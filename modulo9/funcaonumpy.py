import numpy as np

#A funcao array() cria um array NumPy
arr2 = np.array([1,2,3,4,5])

print(arr2)
print(arr2.cumprod())

#A função arange cria um array numpy contendo uma progressão aritmetica a partir de um intervalo - start, stop, step
arr3 = np.arange(0,50,5)
print(arr3)

#cria um array preenchido com zeros
arr4 = np.zeros(10)
print(arr4)

#retorna 1 nas posicoes em diagonal e 0 no restante
arr5 = np.eye(3)
print(arr5)

#os valores passados como parametro, formam uma diagonal
arr6 = np.diag(np.array([1,2,3,4]))
print(arr6)