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

#Pergunta de Negócio 4: Quais São as 10 Cidades com Maior Total de Vendas? Demonstre o resultado através de um gráfico de barras.

# Agrupamos por cidade, calculando o total de vendas e ordenamos listando somente os 10 primeiros registros
df_p4 = df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)

print(df_p4.head(10))

#Plot 
plt.figure(figsize=(16,6))
sns.set_palette('coolwarm')
sns.barplot(data = df_p4,
            y = 'Valor_Venda',
            x = 'Cidade').set(title = 'As 10 cidades com maior total de Vendas')

plt.show()