
print('***********BEM VINDO AO MEU BANCO***********')

menu = '''
    Selecione a opção desejada:

    [d] depósito
    [s] saque
    [e] extrato
    [q] sair

'''

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3


while True:

    escolha = input(menu)

    if escolha == 'd':
        valor = float(input('Digite o valor do depósito: '))

        if valor > 0:
            saldo += valor

            extrato += f'Depósito: R${valor:.2f}\n'
        else:
            print('Não é possível depositar valores negativos')

    elif escolha == 's':

        valor = float(input('Digite o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou. Você não tem saldo o suficiente')

        elif excedeu_limite:
            print('Operação falhou. Você excedeu o limite de R$500.00 por saque')

        elif excedeu_saques:
            print('Operação falhou. O limite de saques foi excedido, para sacar, aguarde até amanhã.')

        else:
            saldo -= valor
            saques += 1 
            extrato += f'Saque: R${valor:.2f}\n'

    elif escolha == 'e':
        print(f'*******EXTRATO******* \n{extrato} \nsaldo: {saldo}')

    elif escolha == 'q':
        print('***********OBRIGADO POR UTILIZAR! VOLTE SEMPRE***********')
        break

    else:
        print('Por favor, selecione uma opção válida')