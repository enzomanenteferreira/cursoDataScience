#criando uma classe chamada circulo
class Circulo():
    #O valor de pi é constante
    pi = 3.14

    #Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5
    def __init__(self,raio = 5):
        self.raio = raio

    #esse método calcula a area
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    #Metodo para gerar um novo raio
    def setRaio(self,novo_raio):
        self.raio = novo_raio

    #Metodo para obter o raio do Circulo
    def getRaio(self):
        return self.raio