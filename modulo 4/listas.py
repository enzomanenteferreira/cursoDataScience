
# estrutura de dados - lista

old_list = [1,2,3,4,5]
new_list = []

#loop para adicionar elementos da lista antiga na nova lista, usando append
for item in old_list:
    new_list.append(item)

print(new_list)

#estender a lista com novos items
cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])

print((cidades.index('Manaus')))

#inserir o valor 110 no indice 2 da lista
cidades.insert(2,110)
