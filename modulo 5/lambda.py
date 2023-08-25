#definindo uma função em 2 linhas de codigo
def potencia(num):
    return num ** 2

print(potencia(5))

#definindo funcao em apenas 1 linha usando lambda(funcao anonima)
potencia = lambda num: num **2

par = lambda x: x%2==0
print(par(8))

first = lambda s: s[0]
print(first("Python"))