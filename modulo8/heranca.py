#criando a classe animal - Super-classe
class Animal:
    def __init__(self):
        print("Animal criado")

    def imprimir(self):
        print("Este é um animal")

    def comer(self):
        print("Hora de comer.")

    def emitir_som(self):
        pass

#Criando classe cachorro - Sub-classe
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au Au!")

#Criando a classe gato - Sub-classe
class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")


#Criando um objeto(Instanciando a classe)
rex = Cachorro()
gato = Gato()

gato.comer()
gato.emitir_som()
rex.emitir_som()