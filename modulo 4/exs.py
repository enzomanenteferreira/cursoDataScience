#exercicio 1 - imprima na tela os numeros de 1 a 10, usando uma lista para armazenar os numeros

list1 = []
numeros = list(range(1,11))

for num in numeros:
    list1.append(num)

print(list1)

#exercicio 2 - crie uma lista de 5 objetos e imprima na tela

list_objetos = ['mouse', 'monitor', 'computador', 'teclado', 'placa-mae']
print(list_objetos)

#exercicio 3 - crie duas string e concatene as duas em uma terceira string

string1 = "hello"
string2 = " world"

string3 = string1 + string2
print(string3)
 
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla1 = (1,2,2,3,4,4,4,5)
print("o numero 4 aparece: ", tupla1.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario = {}
print(dicionario)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario2 = {"chave1":1, "chave2":2, "chave3":3}
#print(dicionario2)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario2["chave4"] = 4
print(dicionario2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicionario3 = {"chave1":10, "chave2":[15,20], "chave3":30}
print("dicionario3: ", dicionario3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

list2 = ['hello world', (1,2), {'chave1':20, 'chave2':40}, 10.20]
print(list2)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

for string in list(range(1,18)):
    print(frase[string])