import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# Carregando o dataset
df = pd.read_csv('dataset.csv')

# Amostra dos dataset
print(df.head())

#####################


#Pergunta de Negócio 3:Qual o Total de Vendas por Estado?Demonstre o resultado através de um gráfico de barras.

# Calculando o total de vendas por estado
df_p3 = df.groupby('Estado')['Valor_Venda'].sum().reset_index()

print(df_p3.head(10))

# Plot
plt.figure(figsize=(16,6))
sns.barplot(data = df_p3,
            y = 'Valor_Venda',
            x = 'Estado').set(title = 'Vendas por Estado')
plt.xticks(rotation = 80)
plt.show()