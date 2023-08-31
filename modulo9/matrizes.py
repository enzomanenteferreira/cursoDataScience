import numpy as np

#criando uma matriz
arr = np.array([[1,2,3],[4,5,6]])

print(type(arr))
print(arr)

#criando uma matriz 2x3 com apenas os numeros "1"
arr2 = np.ones((2,3))
print(arr2)

#lista de listas
lista = [[13,81,22], [0,34,59], [21,48,94]]

#a função matrix cria uma matriz a partir de uma lista de listas
arr3 = np.matrix(lista)
print(arr3)

#indexação da matriz
print(arr3[2,2]) # printa o 3 elemento da 3 linha da matriz

#indexação da matriz
print(arr3[0:3,1]) # no range de 0 a 3 printar os elementos da 1 coluna

arr4 = np.array([[23,76,92,14], [47,35,89,2]], dtype = float)
print(arr4)