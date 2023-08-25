#criando tupla e imprimindo cada valor

tp = (2,3,4)

for i in tp:
    print(i)

#imprimindo cada valor de uma lista
listaString = ["Data", "Science", "Academy"]
for i in listaString:
    print(i)

#numeros pares da lista de numeros
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print(num)


#loop aninhados
lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

#loop externo
for elemento_lista1 in lista1:

    #loop interno
    for elemento_lista2 in lista2:
        print("\n", elemento_lista1 * elemento_lista2)

    print('----')

#o numero 47 aparece nas duas listas?
lista3 = [10,16,24,39,47]
lista4 = [32,89,47,76,12]

#loop externo
for elemento_lista3 in lista3:
    #loop interno
    for elemento_lista4 in lista4:
        if elemento_lista3==47 and elemento_lista4 == 47:
            print("O numero 47 foi encontrado nas duas listas")


lista5 = [24,33,26,90,23]
lista6 = [87,124,120,32,18]
soma = 0
for lista in [lista5,lista6]:
    for num in lista:
        if num % 2 == 0:
            soma+= num
    
print("a soma de numeros pares das duas listas é igual a", soma)


#loop em listas (matrizes) para encontrar o maior numero
matriz = [[42,23,34],[100,215,114],[10.1,98.7,12.3]]
maior_numero = 0

#loop externo 
for linha in matriz:
    #loop interno
    for num in linha:
        #condicional
        if num > maior_numero:
            maior_numero = num

print("maior numero: ", maior_numero)
