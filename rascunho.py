# import unittest   # The test framework

# class Test_TestIncrementDecrement(unittest.TestCase):

#     class Bicicleta():
#         def __init__(self,cor, modelo, ano, valor):
#             self.cor = cor
#             self.modelo = modelo
#             self.ano = ano
#             self.valor = valor

#         def test_buzinar(self):
#             print('Biiiiiii')

#         def test_parar(self):
#             print("Parando bicicleta")

#         def test_correr(self):
#             print("vruuuuuum")

#         def get_cor(self):
#             print(f'{self.cor}')

#         def __str__(self):
#             return f'Classe: {self.__class__.__name__}\ncor: {self.cor}\nmodelo: {self.modelo}'
        
    
# if __name__ == '__main__':
#     unittest.main()

class ControleRemoto:
    def ligar(self):
        pass
    
    def desligar(self):
        pass
class ControleTV(ControleRemoto):
    pass


c1 = ControleTV()
c1.ligar()