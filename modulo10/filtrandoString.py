import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())

#filtrando o dataframe pela coluna segmento com valores que iniciam com as letras 'Con'
print(df[df.Segmento.str.startswith('Con')].head())

#Filtrando o dataFrame pela coluna Segmento com valores que terminam com as metras 'mer'
print(df[df.Segmento.str.endswith('mer')].head())

print(df.Categoria.value_counts())


##Split de String em Dataframes do Pandas
 
#Split da coluna ID_Pedido pelo caracter '-'
print(df['ID_Pedido'].str.split('-'))

#para extrair o ano preciamos especificar o indice da posição que queremos extrair
print(df['ID_Pedido'].str.split('-').str[1])

#fazendo o split da coluna e extraindo o item na posição 2(indice 1)
df['Ano'] = df['ID_Pedido'].str.split('-').str[1]

#printa o dataframe com a nova coluna 'Ano'
print(df)