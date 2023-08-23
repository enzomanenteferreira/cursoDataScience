
#gerar codigo que cria uma lista entre 1 e 100 e imprima os numeros pares, mas somente se o numero for divisivel por 4

#cria a lista com os numeros entre 1 e 100
numeros = list(range(1,101))

#percorre a lista e verifica se o numero é par e divisivel por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)


#usando list comprehension para gerar a lista com os numeros pares e divisiveis por 4
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
#print(pares_div4)