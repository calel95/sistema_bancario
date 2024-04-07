opcao = 0
saldo = 0
quantidade_de_saques_no_dia = 0
#operacao = []
extrato = ''
usuarios = []
contas_corrente = []

def cria_usuario(nome,data_nascimento,cpf,endereco):
    global usuarios
    novo_usuario = (nome,data_nascimento,cpf,endereco)
    usuarios.append(novo_usuario)
    print(usuarios)

def deposito(valor_deposito):
    global extrato
    global saldo
    if valor_deposito >0:
        saldo += valor_deposito
        extrato += f'Depósito: R${valor_deposito},00\n'
    else:
        print("Valor do depósito precisa ser positivo!")
    return extrato, saldo

def saque(valor_saque):
    global extrato
    global saldo
    global quantidade_de_saques_no_dia
    if valor_saque > 500 or quantidade_de_saques_no_dia > 3:
            print("excedeu o limite de saque no valor de 500 reais ou 3 saques diários")
    elif saldo == 0:
        print("Não é possivel realizar operação sem saldo")
    elif saldo < valor_saque:
        print(f"Saldo insuficiente para realizar o saque, seu saldo atual é de R${saldo},00")
    else:
        saldo -= valor_saque
        extrato += f'Saque: R${valor_saque},00\n'
        quantidade_de_saques_no_dia += 1 
    return extrato, quantidade_de_saques_no_dia, saldo

def movimentacoes(saldo, ext=extrato):
     print("\n")
     print(ext)
     print(f"\nSaldo: R$ {saldo},00")

def valida_cpf(cpf):
    global usuarios
    print("CCCCPF", cpf)
    print(usuarios)
    for i in usuarios:
        print(i)
        if cpf == i[2]:
            print("ja existe cpf")
            return True
    return False

while opcao != 7:
    print("""
1 - DEPOSITO
2 - SAQUE
3 - EXTRATO
4 - CRIAR NOVO USUÁRIO
5 - CRIAR NOVA CONTA
6 - LISTAR USUARIOS
7 - SAIR
""")

    opcao = int(input("Opcao:"))

    if opcao == 1:
        valor_deposito = int(input("\nValor do deposito:"))
        deposito(valor_deposito)
    if opcao == 2:
        valor = int(input("Valor do saque:"))
        saque(valor)
    if opcao == 3:
        movimentacoes(saldo,extrato)
    if opcao == 4:
        nome = 'Calel' #input("Nome: ")
        data_nascimento = '19/01/01' #input("Data de Nascimento: ")
        cpf = input("CPF: ")
        while cpf.isdigit() == False or len(cpf) != 11:
            print("CPF precisa receber apenas números e ter 11 digitos!!")
            cpf = input("CPF: ")
        if valida_cpf(cpf) == False:
            #print("ENDERECO")
            rua = 'Luizito' #input("Rua: ")
            numero = '31' #input("Número: ")
            bairro = 'Florida' #input("Bairro: ")
            cidade = 'Goiania' #input("Cidade: ")
            estado = 'MJ' #input("Estado: ")

            endereco = f'{rua}, {numero} - {bairro} - {cidade}/{estado}'
            cria_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        else:
            print("CPF já cadastrado!")
    if opcao == 6:
         print(usuarios)
         for i in usuarios:
              print(i[2])
    elif opcao > 7 or opcao <= 0:
        print("opcao inválida!")