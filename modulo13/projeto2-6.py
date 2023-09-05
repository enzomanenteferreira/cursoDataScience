import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# Carregando o dataset
df = pd.read_csv('dataset.csv')

# Amostra dos dataset
#print(df.head())

#####################

#Pergunta de Negócio 6:Qual o Total de Vendas Por Segmento e Por Ano?

# Convertemos a coluna de data para o tipo datetime para obter o formato adequado
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], dayfirst = True)
#print(df.head())

# Extraimos o ano criando uma nova variavel
df['Ano'] = df['Data_Pedido'].dt.year
#print(df.head())

# Total de vendas por segmento e por ano
df_p6 = df.groupby(['Ano','Segmento'])['Valor_Venda'].sum()
print(df_p6)