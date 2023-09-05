import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Carregando o dataset
df = pd.read_csv('dataset.csv')

# Amostra dos dataset
print(df.head())

# Colunas do conjunto de dados
#print(df.columns)

# Resumo estatistico da coluna com o valor de venda
#print(df['Valor_Venda'].describe())

# Verificando se ha registros duplicados
#print(df[df.duplicated()])

#verificando se ha valores ausentes
#df.isnull().sum()

###################################

#Pergunta de Negócio 1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# Primeiro filtramos o dataframe com os registros da categoria que desejamos
df_p1 = df[df['Categoria'] == 'Office Supplies']

# Agrupamos por cidade e calculamos o total de valor_venda
df_p1_total = df_p1.groupby('Cidade')['Valor_Venda'].sum()

# encontramos a cidade com maior valor de venda
cidade_maior_venda = df_p1_total.idxmax()
print("Cidade com maior valor de venda para 'Office Supplies': ", cidade_maior_venda)

# para conferir o resultado
print(df_p1_total.sort_values(ascending= False))


