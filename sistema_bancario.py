'''REGRAS
1 - precisa ter 3 operacoes, SAQUE, DEPOSITO e EXTRATO
DEPOSITO - Permitido depositar apenas valores positivos; Terá apenas 1 usuário nessa versão, devem ser armazenado em uma variavel e apresentado no extrato
SAQUE - permitido realizar 3 saques diário com limite máximo de 500 reais por saque; Caso usuário sem saldo, 
devera apresentar mensagen informando que não é possivel realizar operação; Todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato
EXTRATO - Apresentar todos os depósitos e saques realizados na conta, e apresentar o saldo atual da conta, utilizando o formato R$ xxx.xx'''

opcao = 0
saldo = 0
quantidade_de_saques_no_dia = 0
#operacao = []
extrato = ''

while opcao != 4:
    print("""
1 - DEPOSITO
2 - SAQUE
3 - EXTRATO
4 - SAIR
""")
    
    opcao = int(input("Opcao:"))

    if opcao == 1:
        valor_deposito = int(input("\nValor do deposito:"))
        if valor_deposito >0:
            saldo += valor_deposito
            #operacao.append(f'Depósito: R${valor_deposito},00')
            extrato += f'Depósito: R${valor_deposito},00\n'
        else:
            print("Valor do depósito precisa ser positivo!")
    if opcao == 2:
        valor_saque = int(input("Valor do saque:"))
        if valor_saque > 500 or quantidade_de_saques_no_dia > 3:
            print("excedeu o limite de saque no valor de 500 reais ou 3 saques diários")
        elif saldo == 0:
            print("Não é possivel realizar operação, sem saldo")
        elif saldo < valor_saque:
            print(f"Saldo insuficiente para realizar o saque, seu saldo atual é de R${saldo},00")
        else:
            saldo -= valor_saque
            #operacao.append(f'Saque: R${valor_saque},00')
            extrato += f'Saque: R${valor_saque},00\n'
            quantidade_de_saques_no_dia += quantidade_de_saques_no_dia + 1 
    if opcao == 3:
        print("\n")
        # for i in operacao:
        #     print(i)
        print(extrato)
        print(f"\nSaldo: R$ {saldo},00")
    elif opcao > 4 or opcao <= 0:
        print("opcao inválida!")
        
