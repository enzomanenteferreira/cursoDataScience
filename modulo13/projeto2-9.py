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
#Pergunta de Negócio 9 :Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?Demonstre o resultado através de gráfico de linha.

# Convertemos a coluna de data para o tipo datetime para obter o formato adequado
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], dayfirst = True)

# Extraimos o mes e o ano e gravamos em uma nova variavel
df['Mes'] = df['Data_Pedido'].dt.month
df['Ano'] = df['Data_Pedido'].dt.year
#print(df.head())

# Agrupamos por ano, mes e segmento e calculamos estatisticas de agregação
df_p9 = df.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
print(df_p9)

# Vamos extarir os niveis
anos = df_p9.index.get_level_values(0)
meses = df_p9.index.get_level_values(1)
segmentos = df_p9.index.get_level_values(2)

# Plot
plt.figure(figsize= (12,6))
sns.set()
fig1 = sns.relplot(kind = 'line',
                   data = df_p9,
                   y = 'mean',
                   x = meses,
                   hue = segmentos,
                   col = anos,
                   col_wrap = 4)

plt.show()