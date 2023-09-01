import pandas as pd
import sklearn
#importando o dataset iris do Scikit-learn
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data = load_iris()

#Carregando o dataset iris como dataframe do Pandas
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']
print(df.head())

# para criar um grafico de linhas com todas as variaveis do dataframe, basta fazer isso:
df.plot()

#scatter plot com duas variaveis
df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')

# graficos mais complexos podem ser criados, como um grafico de area:
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area()

#calculando a media das colunas agrupando pela coluna species e criando um grafico de barras com o resultado
#df.groupby('species').mean().plot.bar()

# a função show mostra as figuras dos graficos criados
plt.show()

## - Outros exemplos de graficos
## - https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html