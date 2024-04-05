# def imprime_endereco(nome, endereco):
#     # Dividir a string de endereço em partes
#     logradouro, cidade,estado = endereco.split(',')

#     # Imprimir os dados
#     print(f"Nome: {nome}")
#     print(f"Endereço: {logradouro}, {cidade}, {estado}")

# # Testar a função
# imprime_endereco("João da Silva", "Rua das Flores, São Paulo, SP")

usuarios = []

# def cria_usuario(endereco,nome,data_nascimento,cpf):
#      print(nome)
#      print(data_nascimento)
#      print(cpf)
#      print(endereco)

#      logradouro, nro, bairro = endereco.split(",")
#      print(logradouro)
#      print(nro)
#      print(bairro)

#cria_usuario(endereco='Rua petri, 31, fatima, cachoeirinha/RS',nome='Calel',data_nascimento='19/01/1895',cpf=2654879897)



def cria_usuario(endereco,nome,data_nascimento,cpf):

    rua,n = endereco.split(",")
    nro,bairro,cidade = n.split("-")
    cidade, estado = cidade.split("/")
    endereco = {'rua': rua, 'numero':nro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}
    print(endereco)

#cria_usuario(endereco='Rua petri, 31 - fatima - cachoeirinha/RS',nome='Calel',data_nascimento="19/01/1900",cpf=123456789)

#endereco = {'rua': 'Rua petri', 'numero':31, 'bairro': 'Fatima', 'cidade': 'cachoeirinha', 'estado': 'RS'}

def cria_usuario_2(endereco,nome,data_nascimento,cpf):
    # rua = input("Rua: ")
    # nro = input("numero: ")
    # bairro = input("bairro: ")
    # cidade = input("cidade: ")
    # estado = input("estado: ")
    print(endereco)
    print(nome)
    print(data_nascimento)
    print(cpf)
    #ende = {'rua': rua, 'numero':nro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}

# rua = input("Rua: ")
# nro = input("numero: ")
# bairro = input("bairro: ")
# cidade = input("cidade: ")
# estado = input("estado: ")

#ende2 = {'rua': rua, 'numero':nro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}

#cria_usuario_2(endereco=ende2, nome='Calel',data_nascimento='19-01-1880',cpf=123456789)

