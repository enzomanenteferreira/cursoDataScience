#manipulação de arquivos em python

#abrindo arquivo para leitura
#arq1 = open("arquivo1.txt", "r")

#lendo o arquivo
#print(arq1.read())

#contar o numero de caracteres
#print(arq1.tell())

#abrindo arquivo para gravação
arq2 = open("arquivo1.txt", "w") # w = write

arq2.write("Aprendendo a programar em python.")
arq2.close()

arq2 = open("arquivo1.txt", "a")
arq2.write("E a metodologia de ensino da data science academy facilita o aprendizado")
arq2.close()

#lendo arquivo gravado
arq2 = open("arquivo1.txt", "r")
print(arq2.read())