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

opcao = 0
saldo = 0
quantidade_de_saques_no_dia = 0
#operacao = []
extrato = ''
usuarios = []
contas_corrente = []

def cria_usuario(nomedata_nascimento,cpf,*endereco):
     ...

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
        deposito(valor_deposito)
    if opcao == 2:
        valor = int(input("Valor do saque:"))
        saque(valor_saque=valor)
    if opcao == 3:
        movimentacoes(saldo,extrato)
    elif opcao > 4 or opcao <= 0:
        print("opcao inválida!")
        
