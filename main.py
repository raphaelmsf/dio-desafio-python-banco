from banco import *


import textwrap



def menu(usuario, conta):
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


    if usuario == '' and conta == '':
      menu = f"""\n
    ================ MENU ================
    Nenhum usuário foi selecionado, gostaria de selecionar um ou criar um novo?

    [nu]\tNovo usuário
    [sel]\tSelecionar usuário

    [q]\tSair
    => """
    elif conta == '' and usuario != '':
      menu = f"""\n
    ================ MENU ================
    Olá {usuario.nome}! Gostaria de selecionar uma conta existente ou criar uma nova?


    [nc]\tNova conta
    [sc]\tSelecionar conta
    [qu]\tSair do usuário

    [q]\tSair do Sistema
    => """

    elif conta != '':
      menu = f"""\n
    ================ MENU ================
    conta:
     {str(conta)}

    [d]\tDepositar
    [s]\tSacar
    [qc]\tSair da conta

    [q]\tSair do Sistema
    => """

    else:
      menu = ''
      print("Ocorreu um erro ao verificar autentiação do usuário ou conta")

    return input(textwrap.dedent(menu))

def novo_usuario(nome, cpf, data_nascimento, endereco, lista_usuarios):
  if cpf not in [usuario._cpf for usuario in lista_usuarios]:
    usuario = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
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

def criar_conta(usuario, lista_contas):
  numero = len(lista_contas) + 1
  conta = ContaCorrente.nova_conta(usuario, numero)
  print("Conta criada com sucesso\n ")
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
    else:
       menu_contas= "Não há contas para este usuário, digite qualquer caractere e aperte enter para voltar"
    return input(menu_contas)

def depositar(usuario, conta, valor):
   deposito = Deposito(valor)
   usuario.realizar_transacao(conta, deposito)
   
def sacar(usuario, conta, valor):
   saque = Saque(valor)
   usuario.realizar_transacao(conta, saque)

def main():
   conta_atual= ''
   usuario_atual = ''
   usuarios = []
   contas = []
   while True:
      opcao = menu(usuario_atual, conta_atual)

      if opcao == 'nu':
         print("Certo! Vamos precisar de alguns dados")
         nome = input("Digite o nome do usuário: ")
         cpf = input("Digite o cpf do usuário: ")
         data_nascimento = input("Digite a data de nascimento do usuário: ")
         endereco = input("Digite o endereco do usuário: ")
         usuario = novo_usuario(nome, cpf, data_nascimento, endereco, usuarios)
         usuarios.append(usuario)
         usuario_atual = usuario
      elif opcao == 'sel':
         numero = selecionar_usuario(usuarios)
         index_usuario = int(numero) - 1
         usuario_atual = usuarios[index_usuario]
      elif opcao == 'nc':
         conta = criar_conta(usuario_atual, contas)
         contas.append(conta)
         conta_atual = conta
      elif opcao == 'sc':
         if len(usuario_atual.contas) > 0:
          numero = selecionar_conta(usuario_atual)
          index_conta = int(numero) - 1
          conta_atual = usuario_atual.contas[index_conta]
         else:
            print("Não há contas para selecionar")
      elif opcao == 'd':
         menu_deposito = f"Saldo disponível: {conta_atual.saldo}\n Quanto deseja depositar? "
         valor = float(input(menu_deposito))
         depositar(usuario_atual, conta_atual, valor)
         print("Depósito realizado com sucesso")
      elif opcao == 's':
         if conta_atual._limite < conta_atual._limite_saques:
          menu_saque = f"Saldo disponível: {conta_atual.saldo}\n Quanto deseja sacar? "
          valor = float(input(menu_saque))
          if valor <= conta_atual.saldo:
            sacar(usuario_atual, conta_atual, valor)
            print("Saque realizado com sucesso")
          else:
            print("Erro! Saldo insuficiente")
         else:
            print("Limite de saques atingido")
      elif opcao == 'q':
         break
      elif opcao == 'qc':
         conta_atual = ''
      elif opcao == 'qu':
         usuario_atual = ''
      else:
         print("Selecione uma opção válida")
        
          
        
            

main()