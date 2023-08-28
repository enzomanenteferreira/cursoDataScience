texto = "Cientista de dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em python.\n"
texto += "E, claro, devem ser proficientes em Data sciencie."


#importando o modulo os
import os

#criando um arquivo
arquivo = open(os.path.join('cientista.txt'),'w')

#gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

arquivo.close()


#ler o arquivo
arquivo = open('cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
