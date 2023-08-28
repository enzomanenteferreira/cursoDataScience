#f = open('arquivos/salarios.csv', 'r')

#data = f.read()

#rows = data.split()
#print(rows)

#full_data = []

#for row in rows:
 #   split_row = row.split(",")
  #  full_data.append(split_row)

#print(full_data)

#printar cada linha do arquivoES
for line in open('arquivos/salarios.csv'):
    print(line)
