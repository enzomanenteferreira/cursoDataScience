#criando classe chamada livro
class livro():

    #O nome do metodo é __init__
    def __init__(self): #construtor

        #atributos são propriedades
        self.titulo = "Sapiens - Uma Breve História da Humanidade"
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")

    
    #metodos sao funçoes que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))


#Criando uma instancia da classe livro
livro1 = livro()

#o objeto Livro1 é do tipo livro
print(type(livro1))

#Atributo do objeto livro1
print(livro1.titulo)
livro1.imprime()

#Criando a classe livro com parametros no método construtor
class livro():
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")

    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo,isbn))

#criando o objeto livro2 que é uma instancia da classe livro
livro2 = livro("O Poder do Habito", 77886611)
print(livro2.titulo, livro2.isbn)



class Algoritmo():
    def __init__(self,tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")

algo1 = Algoritmo(tipo_algo= 'Random Forest')
algo2 = Algoritmo(tipo_algo= 'Deep Learning')

print(algo1.tipo)
print(algo2.tipo)