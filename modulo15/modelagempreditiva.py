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


# preparação dos dados

# prepara a variavel de entrada x
x = np.array(df['horas_estudo_mes'])

# ajusta o shape de x
x = x.reshape(-1,1)

#prepara a variavel alvo
y = df['salario']

# dividir dados em treinamento e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.2, random_state=42)

# cria o modelo de regressao linear
modelo = LinearRegression()

# treina o modelo
modelo.fit(x_treino,y_treino)

# visualiza a reta de regressao linear (previsoes) e os dados reais usados no treinamento
plt.scatter(x,y, color = "blue", label = "Dados Reais Historicos")
plt.plot(x,modelo.predict(x), color = "red", label = "Reta de regressão com as previsoes do modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salario")
plt.legend()
plt.show()

# avalia o modelo nos dados de teste
score = modelo.score(x_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")




# Deploy do Modelo

# define um novo valor para horas de estudo
horas_estudo_novo = np.array([[48]])

# faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"se voce estudar cerca de", horas_estudo_novo, " horas por mes seu salario pode ser igual a", salario_previsto)
