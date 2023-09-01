import pandas as pd
#importando a função DataFrame do Pandas
from pandas import DataFrame

#criando um dicionario
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004,2005,2006,2007,2008],
         'Taxa Desemprego': [1.5,1.7,1.6,2.4,2.7]}

df = DataFrame(dados)

#vizualiza as 5 primeiras linhas
print(df.head())

#Reorganizando as colunas
print(DataFrame(dados,columns = ['Estado', 'Taxa Desemprego', 'Ano']))

#criando outro DataFrame com os mesmos dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados,
                columns=['Estado', 'Taxa Desemprego','Taxa Crescimento','Ano'],
                index = ['estado1','estado2','estado3','estado4','estado5'])

#imprimindo as colunas do dataframe
print(df2.columns)

#imprimindo apenas uma coluna do dataframe
print(df2['Estado'])

#importando o numpy
import numpy as np

#usando o numpy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2)

#resumo estatistico do dataframe
print(df2.describe())