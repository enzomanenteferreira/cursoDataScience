import numpy as np

arr1 = np.arange(1,10)
print(arr1)

#Soma dos elementos do array
print('soma dos elementos do array: ',np.sum(arr1))

#retorna o produto dos elementos
print('produto dos elementos do array: ', np.prod(arr1))

#soma acumulada dos elementos do
print('soma acumulada dos elementos do array: ', np.cumsum(arr1))

#criar 2 arrays
arr2 = np.array([5,8,15])
arr3 = np.array([10,20,30])

#soma dos array
arr4 = np.add(arr2,arr3)
print('soma dos arrays 2 e 3: ', arr4)

#cria duas matrizes
arr5 = np.array([[1,2], [3,4]])
arr6 = np.array([[5,6], [0,7]])

print(arr5)

print(arr6)

#Multiplicar as duas matrizes
#arr7 = arr5 @ arr6 - faz a mesma coisa que a função dot
arr7 = np.dot(arr5,arr6)
print(arr7)


#cria um array
arr8 = np.diag(np.arange(5)) # coloca os valores de 0 a 5 na diagonal de uma matriz
print(arr8)

#cria 2 arrays
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])

#comparação item a item
print(a == b)

#comparação global
print(np.array_equal(arr5,arr6))

#criando um array
arr9 = np.array([[1,2,3,4],[5,6,7,8]])

print(arr9)
#acahatando a matriz usando a função flatten
arr9 = arr9.flatten()
print(arr9)