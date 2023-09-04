import numpy as np
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

#valores randomicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2

#variaveis
flag_fumante = np.random.rand(n) < pct_smokers
#print(flag_fumante)
idade = np.random.normal(40,10,n)
altura = np.random.normal(170,10,n)
peso = np.random.normal(70,10,n)

#dataFrame
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

#cria os dados para a variavel flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False:'Não Fumante'})

print(dados.head())

#Style
sea.set(style = "ticks")

#lmplot
sea.lmplot(x = 'altura',
           y = 'peso',
           data = dados, 
           hue = 'flag_fumante',
           palette=['tab:blue', 'tab:orange'],
           height = 7)

#labels e titulo
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e não fumantes')

#Remove as bordas
sea.despine()

#Show
plt.show()