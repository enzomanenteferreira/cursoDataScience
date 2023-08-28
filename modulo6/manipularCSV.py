#importando modulo csv
import csv

with open('numeros.csv','w') as arquivo:
        #cria o objeto de gravação
        writer = csv.writer(arquivo)

        #grava no arquivo linha a linha
        writer.writerow(('nota1','nota2','nota3'))
        writer.writerow((63,87,100))
        writer.writerow((200,120,300))
        writer.writerow((150,210,500,302,199))

#leitura de arquivos csv
with open('numeros.csv','r', encoding='utf8',newline = '\r\n') as arquivo:
        #cria o objeto de leitura
        leitor = csv.reader(arquivo)
        
        #loop
        for x in leitor:
            print(x)