#Superclasse
class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

#Subclasse
class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando")

    def frear(self):
        print("O carro está freando")

#Subclasse
class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando.")
    
    def frear(self):
        print("A moto está freando")

class Aviao(Veiculo):
    def acelerar(self):
        print("O aviao está acelerando.")

    def frear(self):
        print("O avião está freando.")
    
    def decolar(self):
        print("O avião está decolando")


#cria os Objetos
lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

#loop
for item in lista_veiculos:
    #O método acelerar tem comportamento diferente dependendo do tipo de objetoo
    item.acelerar()

    #O metodo frear tem comportamento diferente dependendo do tipo de objeto
    item.frear()

    # Executamos o metodo decolar somento se o objeto for instancia da classe aviao
    if isinstance(item,Aviao):
        item.decolar()

    print("---")