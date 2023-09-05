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


#Pergunta de Negócio 5:Qual Segmento Teve o Maior Total de Vendas? Demonstre o resultado através de um gráfico de pizza.

df_p5 = df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda',
                                                                              ascending= False)

print(df_p5.head())


# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

# Plot

# Tamanho da figura
plt.figure(figsize= (16,6))

# Grafico de pizza
plt.pie(df_p5['Valor_Venda'],
        labels = df_p5['Segmento'],
        autopct= autopct_format(df_p5['Valor_Venda']),
        startangle= 90)

# Limpa o circulo central
centre_circle = plt.Circle((0,0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Labels e anotaçoes
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_p5['Valor_Venda']))), xy = (-0.25,0))
plt.title('Total de Vendas por Segmento')
plt.show()