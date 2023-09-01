import pandas as pd

#primeiro deve-se importar um dataset
df = pd.read_csv("dataset.csv")
print(df.head(5))

#checando os valores minimos e maximo da coluna Valor_Venda
print(df.Valor_Venda.describe())

# Gerando um novo dataFrame apenas com o intervalo de vendas entre 229 e 10000
df2 = df.query('229 < Valor_Venda < 10000')

# Confirmando os valores minimo e maximo
print(df2.Valor_Venda.describe())

#Gerando um novo dataframe apenas com os valores de venda acima da media
df3 = df2.query('Valor_Venda > 766')
print(df3.head())

print(df.shape)

#aplicando o filtro para verificar a ocorrencia de diversos valores em uma coluna
print(df[df['Quantidade'].isin([5,7,9,11])])