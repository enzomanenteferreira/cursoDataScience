#List comprehension que imprime os numeros menores que 5 em um intervalo de 1 a 10
lista_numeros = [x for x in range(10) if x<=5]
print(lista_numeros)

#loop para buscar palavras com letra "m"
lista_frutas = ["banana", "abacate", "melancia", "cereja", "manga"]
nova_lista = []
for x in lista_frutas:
    if "m" in x:
        nova_lista.append(x)

print(nova_lista)

#mesmo resultado mas com list comprehension
nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)

#dicionario comprehension
#dicionario de alunos e notas
dict_alunos = {'bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

#criando um novo dicionario e imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status)