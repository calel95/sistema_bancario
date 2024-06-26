'''REGRAS DA VERSÃO 1
1 - precisa ter 3 operacoes, SAQUE, DEPOSITO e EXTRATO
DEPOSITO - Permitido depositar apenas valores positivos; Terá apenas 1 usuário nessa versão, devem ser armazenado em uma variavel e apresentado no extrato
SAQUE - permitido realizar 3 saques diário com limite máximo de 500 reais por saque; Caso usuário sem saldo, 
devera apresentar mensagen informando que não é possivel realizar operação; Todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato
EXTRATO - Apresentar todos os depósitos e saques realizados na conta, e apresentar o saldo atual da conta, utilizando o formato R$ xxx.xx
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
REGRAS DA VERSÃO 2
1 - Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário e cadastrar conta bancária
2 - Saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno: saldo e extrato. Exemplo.: saque(saldo=50, valor=90...).
3 - Depósito deve receber os argumentos apenas por posição. Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato. Exemplo.:deposito(50)
4 - Extrato deve receber os argumentos por posição e nome. Argumentos posicionais: saldo, argumentos nomeados: extrato

Criação dos usuários - O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: 
logradouro, nro - bairro - cidade/estado. Deve ser armazenado apenas números do CPF. Não pode cadastrar 2 usuários com mesmo CPF

Criação conta corrente - O programa deve armazenar contas em uma lista, uma conta é composta por: agência, numero da conta e usuario. O numero da conta e sequencial, iniciando com 1.
O numero da agencia e fixo: "0001". O usuario pode ter mais de uma conta, mas uma conta pertence somente a um usuario.

Dica: pra vincular usuario a conta, filtrar a lista de usuarios buscando pelo CPF informado para cada usuario da lista
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

import random

opcao = 0
saldo = 0
quantidade_de_saques_no_dia = 0
#operacao = []
extrato = ''
usuarios = []
contas_corrente = []
conta = 1
usuario_nao_existe = True
#cpf = '1'

     

def cria_conta_corrente(agencia,numero_conta,usuario):
    global usuarios
    global contas_corrente
    nova_conta = (agencia,numero_conta,usuario)
    contas_corrente.append(nova_conta)
     
def cria_usuario(nome,data_nascimento,cpf,endereco):
     global usuarios
     #endereco = dict(endereco)
     novo_usuario = (nome,data_nascimento,cpf,endereco)
     usuarios.append(novo_usuario)
     #print(usuarios)

def deposito(valor_deposito):
    global extrato
    global saldo
    if valor_deposito >0:
        saldo += valor_deposito
        #operacao.append(f'Depósito: R${valor_deposito},00')
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
        #operacao.append(f'Saque: R${valor_saque},00')
        extrato += f'Saque: R${valor_saque},00\n'
        quantidade_de_saques_no_dia += quantidade_de_saques_no_dia + 1 
    return extrato, quantidade_de_saques_no_dia, saldo

def movimentacoes(saldo, ext=extrato):
     print("\n")
     print(ext)
     print(f"\nSaldo: R$ {saldo},00")

def valida_cpf(cpf):
    global usuarios
    #print(usuarios)
    for i in usuarios:
        #print(i)
        if cpf == i[2]:
            print("Já existe usuário cadastrado com o mesmo CPF!!", i)
            return True
    return False

def valida_usuario(usuario_da_conta):
    global usuarios
    for i in usuarios:
        #print(i[2])
        if usuario_da_conta == i[2]:
            return True
    return False
        
while opcao != 8:
    print("""
1 - DEPOSITO
2 - SAQUE
3 - EXTRATO
4 - CRIAR NOVO USUÁRIO
5 - CRIAR NOVA CONTA
6 - LISTAR USUARIOS
7 - LISTAR CONTAS
8 - SAIR
""")
    
    opcao = int(input("Opcao:"))

    if opcao == 1:
        valor_deposito = int(input("\nValor do deposito:"))
        deposito(valor_deposito)
    if opcao == 2:
        valor = int(input("Valor do saque:"))
        saque(valor_saque=valor)
    if opcao == 3:
        movimentacoes(saldo,extrato)
    if opcao == 4:
        nome = 'Calel' #input("Nome: ")
        data_nascimento = '19/01/01' #input("Data de Nascimento: ")
        cpf = input("CPF: ")
        while cpf.isdigit() == False:
             print("CPF precisa receber apenas números!!")
             cpf = '123456'
        if not valida_cpf(cpf):
            #print("ENDERECO")
            rua = 'Luizito' #input("Rua: ")
            numero = '31' #input("Número: ")
            bairro = 'Florida' #input("Bairro: ")
            cidade = 'Goiania' #input("Cidade: ")
            estado = 'MJ' #input("Estado: ")

            endereco = f'{rua}, {numero} - {bairro} - {cidade}/{estado}'
            cria_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        else:
            print("Só é permitido um CPF por usuário!!")
    if opcao == 5: 
        agencia = '0001'
        usuario_da_conta = input('Digite seu CPF para cadastrar uma conta:')
        # for i in usuarios:
        #     #print(i[2])
        #     if usuario_da_conta == i[2]:
        #         usuario_nao_existe = False
        if not valida_usuario(usuario_da_conta):
            print("\nNão é possível cadastrar conta sem usuário cadastrado!!")
        if valida_usuario(usuario_da_conta) == True:
            for i in usuarios:
                #print(i[2])
                if usuario_da_conta == i[2]:
                    print(f"Conta criada e vinculado ao usuário cadastrado: {i}")
                    conta += 1
                    cria_conta_corrente(agencia=agencia,numero_conta=conta,usuario=i)
    if opcao == 6:
         #print(usuarios)
         for i in usuarios:
              print(i)
    if opcao == 7:
         print(contas_corrente)
    elif opcao > 8 or opcao <= 0:
        print("opcao inválida!")
        
