#importando o modulo JSON
import json

#criando um dicionario
dict_guido = {'nome': 'Guido van rossum',
              'linguagem': 'Python',
              'similar': ['c','Modula-3','lisp'],
              'users': 1000000}

for k,v in dict_guido.items():
    print(k,v)

#convertendo o dicionario para um objeto JSON
json.dumps(dict_guido)

#criando um arquivo JSON
with open('dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

#leitura de arquivos JSON
with open('dados.json','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)
print(dados['nome'])