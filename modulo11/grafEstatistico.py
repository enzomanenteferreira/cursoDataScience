import random
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sea

# Carregando um dos datasets que vem com o seaborn
dados = sea.load_dataset("tips")
print(dados)

# O metodo joinplot cria plot de 2 variaveis com graficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')

# O metodo implot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")

#plt.show()

# Construindo um DataFrame com pandas
df = pd.DataFrame()

# Alimentando o dataframe com valores aleatorios
df['idade'] = random.sample(range(20,100),30)
df['peso'] = random.sample(range(55,150),30)

print(df)

# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg=True)

#plt.show()

#kdeplot
sea.kdeplot(df.idade)

#kdeplot
sea.kdeplot(df.peso)

#distplot
sea.distplot(df.peso)

#histograma
plt.hist(df.idade, alpha = .3)
sea.lmplot(df.idade)

# Box Plot
sea.boxplot(df.idade, color = 'm')