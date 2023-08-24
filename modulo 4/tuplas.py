#criando tuplas

tupla1 = ("Geografia",23, "Elefantes", 9.8, 'Python')
print(tupla1)

#tuplas nao suportam append()
#tuplas nao suportam atribuição de item

#usando a função list() para converter uma tupla para uma lista
t2 = ('A', 'B', 'C')

lista1 = list(t2)
lista1.append('D')

#usando a função tuple() para converter a lista para tupla 
t2 = tuple(lista1)
print(lista1)