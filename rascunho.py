# def imprime_endereco(nome, endereco):
#     # Dividir a string de endereço em partes
#     logradouro, cidade,estado = endereco.split(',')

#     # Imprimir os dados
#     print(f"Nome: {nome}")
#     print(f"Endereço: {logradouro}, {cidade}, {estado}")

# # Testar a função
# imprime_endereco("João da Silva", "Rua das Flores, São Paulo, SP")

usuarios = []

def cria_usuario(endereco,nome,data_nascimento,cpf):
     print(nome)
     print(data_nascimento)
     print(cpf)
     print(endereco)

     logradouro, nro, bairro = endereco.split(",")
     print(logradouro)
     print(nro)
     print(bairro)

#cria_usuario(endereco='Rua petri, 31, fatima, cachoeirinha/RS',nome='Calel',data_nascimento='19/01/1895',cpf=2654879897)


end = 'Rua petri, 31 - fatima - cachoeirinha/RS'

a = end.split(",")
#b,c,d = 
print(a)