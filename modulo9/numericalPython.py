import numpy as dsa

#criando array a partir de uma lista Python
arr1 = dsa.array([10,21,32,43,48,15,76,57,85])
print(arr1)

print(arr1[0:4])

print(arr1[1:4+1])

#cria uma lista de indices
indices = [1,2,5,6]

#imprimindo os elementos dos indices
print(arr1[indices])

#cria uma mascara booleana para os elementos pares
mask = (arr1 % 2 == 0)
print(mask)
print([mask])