import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas nos bancos de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
cursor.execute(sql_query)

#Visualiza o resultado
print(cursor.fetchall())

# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa' # retorna todas as colunas dessa tabela

# Executa a query no banco de dados
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# printa o resultado
print(nomes_colunas)

# Retorna os dados da execução da query
dados = cursor.fetchall()

#vizualiza os dados
#print(dados)

# Cria uma instrução SQL para calcular a media de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query2)

#Visualiza o resultado
#print(cursor.fetchall())

# Cria uma instrução SQL para calcular a media de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

# Executa a query no banco de dados
cursor.execute(query3)

#visualiza o resultado
#print(cursor.fetchall())
#for x in cursor.fetchall():
 #   print(x)


# Cria uma instrução SQL para calcular a media de unidades vendidas por produto quando o valor unitario for maior que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
    FROM tb_vendas_dsa
    WHERE Valor_Unitario > 199
    GROUP BY Nome_Produto"""

# Executa a query no banco de dados
cursor.execute(query4)

#visualiza o resultado
for y in cursor.fetchall():
    print(y)

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()