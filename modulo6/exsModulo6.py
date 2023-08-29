import math
# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

lista = [1,2,3]

for i in lista:
    pot = i ** 3
    print(pot)


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)


result = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print(i)


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]

transposta = [[row[i] for row in matrix] for i in range(2)]
print(transposta)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def quadrado(x):
    return (x**2)

def cubo(x):
    return(x**3)

funcoes = [quadrado,cubo]

for i in lista:
    valor = map(lambda x: x(i), funcoes)
    print(list((valor)))



# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]
print(list(map(pow,listaA,listaB)))

# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
range(-5, 5)

def verificaNeg(num):
    if num<0:
        return True
    else:
        return False

print(list(filter(verificaNeg,range(-5,5))))

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print(list(filter(lambda x: x in a, b)))


# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1,d2):
    dictTemp = {}

    for d1key, d2val in zip(d1.keys(),d2.values()):
        dictTemp[d1key] = d2val
        
    return dictTemp

dict3 = trocaValores(dict1,dict2)
print(dict3)



# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for indice, valor in enumerate(lista):
    if indice <=5 :
        continue
    else:
        print(list(valor))


# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

match = re.findall(r'Data Science (\w+)', texto)
print("As palavra seguida por data e science são:", match[0])