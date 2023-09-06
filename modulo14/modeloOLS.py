import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# carrega o dataset
df = pd.read_csv('dataset.csv')

#print(df.head())

# definindo a variavel dependente
y = df["valor_aluguel"]

# definindo a variavel independente
x = df["area_m2"]

# O statsmodels requer a adição de uma constante a variavel independente
x = sm.add_constant(x)

# criando o modelo - A função OLS(Ordinary least squares) é usada para ajustar um modelo de regressão linear, minimizando
# a soma dos erros quadraticos entre os valores observados e os valores previstos pelo modelo
modelo = sm.OLS(y,x)

# Treinamento do modelo
resultado = modelo.fit()

print(resultado.summary())

# Plot
plt.figure(figsize = (12,8))
plt.xlabel("area_m2", size = 16)
plt.ylabel("valor_aluguel", size = 16)
plt.plot(x["area_m2"], y, "o", label = "Dados_Reais")
plt.plot(x["area_m2"], resultado.fittedvalues, "r-", label = "Linha de regressão ( Previsões do Modelo)")
plt.legend(loc = "best")
plt.show()