import numpy as np
import pandas as pd
from pandas import DataFrame

#criando um dicionario
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004,2005,2006,2007,2008],
         'Taxa Desemprego': [1.5,1.7,1.6,2.4,2.7]}

df = DataFrame(dados)

#criando outro DataFrame com os mesmos dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados,
                columns=['Estado', 'Taxa Desemprego','Taxa Crescimento','Ano'],
                index = ['estado1','estado2','estado3','estado4','estado5'])

#usando o numpy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2['estado2':'estado4'])

print(df2[df2['Taxa Desemprego'] < 2 ])