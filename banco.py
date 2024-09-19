
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco=None, contas=[]):
        self._endereco = endereco
        self._contas = contas

    @property
    def contas(self):
        return self._contas

    # As operações de saque e deposito serão feitas inicialmente a partir deste método
    def realizar_transacao(self, conta, transacao):
        if type(transacao) == Saque:
            transacao.registrar(conta)
        elif type(transacao) == Deposito:
            transacao.registrar(conta)
        else:
            print(f'Erro! A transação deve ser do tipo saque ou depósito. Tipo atual: {type(transacao)}')

    # Adiciona uma conta à lista _contas
    def adicionar_conta(self, conta):
        if conta not in self._contas:
            self._contas.append(conta)
        else:
            print('Esta conta já está registrada')

class PessoaFisica(Cliente):
    def __init__(self, endereco=None, contas=[], cpf=None, nome=None, data_nascimento=None):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def contas(self):
        return self._contas

    @property
    def nome(self):
        return self._nome

class Historico:
    def __init__(self, historico=''):
        self._historico = historico

    def adicionar_transacao(self, transacao):
        agora = datetime.now()
        agora_formatado = agora.strftime("%d/%m/%Y %H:%M")
        valor = transacao.valor
        if type(transacao) == Saque:
            self._historico += f"-R${valor}. {agora_formatado}\n"
        elif type(transacao) == Deposito:
            self._historico += f"+R${valor}. {agora_formatado}\n"
        else:
            print('Erro: Transação Inválida')

    def __str__(self):
        return self._historico

class Conta:
    def __init__(self, saldo=0, numero=0, cliente=None):
        self._saldo = saldo
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    # Cria uma nova conta e adiciona à lista contas do cliente
    @classmethod
    def nova_conta(cls, cliente, numero):
        conta = cls(cliente=cliente, numero=numero)
        cliente.adicionar_conta(conta)
        return conta

    # retira o valor da conta
    def sacar(self, valor):
        self._saldo -= valor
        saque = Saque(valor)
        self._historico.adicionar_transacao(saque)
        return True


    # adiciona o valor à conta
    def depositar(self, valor):
        self._saldo += valor
        deposito = Deposito(valor)
        self._historico.adicionar_transacao(deposito)
        return True

    # retorna uma string que se refere aos dados da conta
    def __str__(self):
        return f'''saldo: R${self.saldo}
        numero: {self._numero}
        agencia: {self._agencia}
        cliente: {self._cliente.nome}
        historico: {str(self._historico)}'''

class ContaCorrente(Conta):
    def __init__(self, saldo=0, numero=0, cliente=None):
        super().__init__(saldo, numero, cliente)
        self._limite = 0
        self._limite_saques = 3

    @property
    def numero(self):
        return self._numero
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if self._limite < self._limite_saques:
            self._saldo -= valor
            saque = Saque(valor)
            self._historico.adicionar_transacao(saque)
            self._limite += 1
            return True
        else:
            print(f"Limite de saques ultapassado. O limite total de saques é {self._limite_saques}\n")




class Transacao(ABC):

    @abstractmethod
    def registrar():
        pass

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor


    def registrar(self, conta):
        saldo = conta.saldo
        if self._valor > 0:
            deposito = conta.depositar(self._valor)
            if deposito:
                print('Depósito realizado com sucesso')
            else:
                print('Transação falhou')
        else:
            print('O valor a se depositar deve ser maior que 0')


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor


    def registrar(self, conta):
        saldo = conta.saldo
        if self._valor <= saldo:
            saque = conta.sacar(self._valor)
            if saque:
              print(f"Saque realizado com sucesso! Saldo atual: R${self._valor}")
        else:
            print("Erro: Saldo insuficiente!")