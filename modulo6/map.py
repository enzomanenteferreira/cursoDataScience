#a função map aplica uma determinada função a cada elemento de uma estrutura de dados iterável, (como uma lista, tupla ou outro objeto iteravel)

#função python que retorna um numero ao quadrado
def potencia(x):
    return x**2

numeros = [1,2,3,4,5]

numeros_ao_quadrado = list(map(potencia,numeros))

print(numeros_ao_quadrado)

#criando duas funções

#função 1 - recebe uma temperatura como parametro e retorna a temperatura em fahrenheit
def fahrenheit(T):
    return((float(9)/5)*T + 32)

#função 2 - recebe uma temperatura como parametro e retorna a temperatura em celsius
def celsius(T):
    return((float(5)/9)* (T-32))

#criando uma lista
temperaturas = [0,22.5,40,100]

#aplicando a função a cada elemento da lista de temperaturas
#a função map retorna um iterator
print(map(fahrenheit,temperaturas))

#função map() retornando a lista de temperaturas convertidas em fahrenheit
print(list(map(fahrenheit,temperaturas)))

#Usando um loop for para imprimir o resultado da função map()
for temp in map(celsius,temperaturas):
    print(temp)

#somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]

print(list(map(lambda x,y:x+y, a,b)))