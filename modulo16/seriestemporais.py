# Analise de series temporais em python
# Usando dados históricos das vendas ao longo de 2023 seria possivel prever o total de vendas em janeiro/2024?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# carregando dataset
df = pd.read_csv('dataset.csv')

#print(df.head())

# Converte a coluna de Data no tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

#print(df.head())

# Converter o dataframe em uma serie temporal com a data como indice
serie_temporal = df.set_index('Data')['Total_Vendas']
#print(serie_temporal)

# Fornece a frequencia da serie temporal(diaria, neste caso)
serie_temporal = serie_temporal.asfreq('D')
#print(serie_temporal)


# Analise exploratoria
# cria o grafico da serie temporal (sem formatação)
plt.figure(figsize=(12,6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Serie temporal de vendas')
plt.grid(True)
#plt.show()

#cria o modelo
modelo = SimpleExpSmoothing(serie_temporal)

# Treinamento (ajuste) do modelo
modelo_ajustado = modelo.fit(smoothing_level=0.2)

# extrai o svalores previstos pelo modelo
suavizacao_exponencial = modelo_ajustado.fittedvalues

# Plot
plt.figure(figsize=(12,6))
plt.plot(serie_temporal, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()
plt.show()

# Fazer previsões
num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps = num_previsoes)
print('Previsão do Total de Vendas para Janeiro/2024:', round(previsoes[0],4))