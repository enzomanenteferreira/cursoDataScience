#Função zip agrupa elementos de multiplas estruturas de dados iteraveis como (lista,tuplas, ou outros objetos iteraveis) junto em pares

#criando duas listas

x = [1,2,3]
y = [4,5,6]

#unindo as listas, em python3 retorna um iterator
print(list(zip(x,y)))

#criando 2 dicionarios
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

print(list(zip(d1,d2)))

#criando uma função para trocar valores entre 2 dicionarios
def trocaValores(d1,d2):
    dicTemp = {}
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp

print(trocaValores(d1,d2))