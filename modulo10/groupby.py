import pandas as pd

#primeiro deve-se importar um dataset
df = pd.read_csv("dataset.csv")

print(df[['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).mean())

#agregação Multipla com Groupby

#aplicamos o group by
print(df[['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).agg(['mean','std','count']))