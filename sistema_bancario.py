menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o Valor que deseja depositar: "))
        
        if valor > 0:
                saldo += valor
                extrato += f"deposito: R${valor: .2f}\n"
        
        else:
             print('Operação Inválida, Por favor coloque um valor válido.')
            

    elif opcao == 's':
        valor = float(input('Informe o Valor que deseja Sacar: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Não foi Possivel Completar a Operação, Você não contém saldo suficiente.')

        elif excedeu_limite:
            print('Não foi possivel completar a operação, o valor excede o limite')
        
        elif excedeu_saques:
            print('Não foi possivel completar a operação, Numero de saques ja foi excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print('Operação Falhou, Numero informado é inválido. ')

    elif opcao == 'e':
        print("\n ================ EXTRATO ================")
        if not extrato:
            print("não foram realizadas movimentação")
        else:
            print(f'\nSaldo: R${saldo:.2f}')
        print("==========================================")

    elif opcao == 'q':
        print('Sair')
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")

