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

#Pergunta de Negócio 7 :Os  gestores  da  empresa  estão  considerando conceder  diferentes  faixas  de  descontos
#e gostariam de fazer uma simulação com base na regra abaixo:Se o Valor_Venda for maior que 1000 recebe 15% de desconto.Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
#Quantas Vendas Receberiam 15% de Desconto?

df['Desconto'] = np.where(df['Valor_Venda'] > 1000,0.15,0.10)

print(df.head())

# Total por cada valor da variavel
print(df['Desconto'].value_counts())

print('No total 457 Vendas receberiam desconto de 15%.')


#Pergunta de Negócio 8 :Considere  Que  a  Empresa  Decida  Conceder  o  Desconto  de  15%  do  Item  Anterior.  Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

# Criamos uma coluna calculando o valor de venda menos o desconto
df['Valor_Venda_Desconto'] = df['Valor_Venda'] - (df['Valor_Venda'] * df['Desconto'])

print(df.head())

# Filtrando as vendas antes do desconto de 15%
df_p8_vendas_antes_desconto = df.loc[df['Desconto'] == 0.15, 'Valor_Venda']

# Filtrando as vendas depois do desconto de 15%
df_p8_vendas_depois_desconto = df.loc[df['Desconto'] == 0.15, 'Valor_Venda_Desconto']

# Calcula a media das vendas antes do desconto de 15%
media_vendas_antes_desconto = df_p8_vendas_antes_desconto.mean()

# Calcula a media das vendas depois do desconto de 15%
media_vendas_depois_desconto = df_p8_vendas_depois_desconto.mean()

print("Media das vendas antes do desconto de 15%:", round(media_vendas_antes_desconto,2))

print("Media das vendas depois do desconto de 15%", round(media_vendas_depois_desconto,2)) 