import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')

# abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

#executa a query no banco de dados
cursor.execute(query)

dados = cursor.fetchall()

#for x in cursor.fetchall():
 #   print(x)


# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido',
                                    'ID_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])


print(df.head())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# Calcula a media de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()
print(media_unidades_vendidas)

# Calcula a media de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()

# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))

# Retorna a media de unidades vendidas por produto se o valor unitario for maior do que 199
print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean())