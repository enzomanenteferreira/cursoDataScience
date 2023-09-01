import pandas as pd

#primeiro deve-se importar um dataset
df = pd.read_csv("dataset.csv")

print(df.head(5))

#funcao isna() procura se tem valor ausentes
print(df.isna().sum())

#extraimos a moda da coluna Quantity
moda = df['Quantidade'].value_counts().index[0]
print('O numero que aparece com mais frequencia na coluna quantidade eh: ', moda)

#por fim, preenchemos os valores NA com a moda
df['Quantidade'].fillna(value = moda, inplace = True) ## inplace = True altera no Dataframe
#print(df.isna().sum())
print(df)