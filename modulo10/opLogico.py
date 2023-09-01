import pandas as pd

#primeiro deve-se importar um dataset
df = pd.read_csv("dataset.csv")

#filtrando as vendas que ocorreram para o segmento de Home Office e na regiao south
print(df[(df.Segmento == 'Home Office') & (df.Regiao == 'South')].head())

#filtrando as vendas que ocorreram para o segmento de Home Office ou na regiao south
print(df[(df.Segmento == 'Home Office') | (df.Regiao == 'South')].tail())

#filtrando as vendas que não ocorreram para o segmento de home office e nem na regiao south
print(df[(df.Segmento != 'Home Office') & (df.Regiao != 'South')].sample(5))