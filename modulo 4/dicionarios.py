 # exemplo lista
estudantes_lista = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]

#exemplo dicionario
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
#print(estudantes_dict["Ronaldo"])

#dicionario de listas
dict = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha','fraldinha', 'alcatra']}

#print(dict['chave3'])

#acessar um item da lista, dentro do dicionario
print(dict['chave3'][1].upper())

#operacao com item da lista
print(dict['chave2'][0]-2)