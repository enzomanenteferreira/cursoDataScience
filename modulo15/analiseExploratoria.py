#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carrega o dataset
df = pd.read_csv('dataset.csv')
#print(df.head())
#print(df.info())

# preparação dos dados

# prepara a variavel de entrada x
x = np.array(df['horas_estudo_mes'])

# ajusta o shape de x
x = x.reshape(-1,1)

#prepara a variavel alvo
y = df['salario']

# grafico de dispersao entre x e y
plt.scatter(x,y,color = "blue", label = "Dados Reais Historicos")
plt.xlabel("Horas de estudo")
plt.ylabel("Salario")
plt.legend()
#plt.show()


# dividir dados em treinamento e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.2, random_state=42)

print(x_treino.shape)
print(x_teste.shape)
print(y_treino.shape)
print(y_teste.shape)