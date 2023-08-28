#A função reduce() aplica uma determinada função binaria a pares consecutivos de elementos em uma estrutura de dados iteravél(como uma lista,tupla, ou outro objeto), reduzindo-a a um unico valor
from functools import reduce

#criando uma lista
lista = [100,200,350,760]

#função
def soma(a,b):
    return a+b

#usando reduce como uma função e uma lista, a função vai retornar o valor maximo
print(reduce(soma,lista))

max_find = lambda a,b: a if(a>b) else b

print(reduce(max_find,lista))
