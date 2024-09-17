from banco import *


import textwrap


conta_atual= ''
usuario_atual = ''
usuarios = []
contas = []

def menu():
    # menu = """\n
    # ================ MENU ================
    # [d]\tDepositar
    # [s]\tSacar
    # [e]\tExtrato
    # [nc]\tNova conta
    # [lc]\tListar contas
    # [nu]\tNovo usuário
    # [sel]\tSelecionar usuário
    # [q]\tSair
    # => """


    if usuario_atual == '' and conta_atual == '':
      menu = f"""\n
    ================ MENU ================
    Nenhum usuário foi selecionado, gostaria de selecionar um ou criar um novo?

    [nu]\tNovo usuário
    [sel]\tSelecionar usuário
    [q]\tSair
    => """
    elif conta_atual == '' and usuario_atual != '':
      menu = f"""\n
    ================ MENU ================
    Olá {usuario_atual.nome}! Gostaria de selecionar uma conta existente ou criar uma nova?


    [nc]\tNova conta
    [lc]\tSelecionar conta
    [q]\tSair
    => """

    elif conta_atual != '':
      menu = f"""\n
    ================ MENU ================
    conta:
     {str(conta_atual)}

    [d]\tDepositar
    [s]\tSacar
    [h]\tExibir Histórico

    [q]\tSair
    => """

    else:
      menu = ''
      print("Ocorreu um erro ao verificar autentiação do usuário ou conta")

    return input(textwrap.dedent(menu))

def novo_usuario(nome, cpf, data_nascimento, endereco):
  if cpf not in [usuario._cpf for usuario in usuarios]:
    usuario = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
    usuarios.append(usuario)
    print(f'Usuário {usuario.nome} criado com sucesso.')
    return usuario
  else:
    print("Este usuário já existe")

def selecionar_usuario(usuarios):
  lista_nomes = []
  menu_nomes = 'Selecione seu usuário digitando o respectivo número:\n'
  for usuario in usuarios:
    nome = usuario.nome
    lista_nomes.append(nome)

  for nome in lista_nomes:
    numero = lista_nomes.index(nome) + 1
    numero = str(numero)
    menu_nomes += '\n' + numero +' ' + nome + '\n'

  return int(input(menu_nomes))

def criar_conta(usuario):
  numero = len(contas) + 1
  conta = ContaCorrente.nova_conta(usuario, numero)
  print("Conta criada com sucesso\n ")
  print(conta)
  return conta

def selecionar_conta(usuario):
    lista_contas = usuario.contas
    menu_contas = ''
  
    if len(lista_contas) > 0:
        menu_contas = 'Selecione sua conta digitando o respectivo número:\n'
        for conta in lista_contas:
            numero = lista_contas.index(conta) + 1
            numero = str(numero)
            numero_conta = conta.numero
            menu_contas += '\n[{}] conta {} tipo: Corrente \n'.format(numero, numero_conta)
        menu_contas = input(menu_contas)
    return menu_contas

def depositar(usuario, conta, valor):
   deposito = Deposito(valor)
   usuario.realizar_transacao(conta, deposito)
   
def sacar(usuario, conta, valor):
   saque = Saque(valor)
   usuario.realizar_transacao(conta, saque)


