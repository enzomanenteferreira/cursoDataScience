import pandas as pd
import matplotlib.pyplot as plt


# Carregando o dataset
df = pd.read_csv('dataset.csv')

# Amostra dos dataset
print(df.head())

#####################

#Pergunta de Negócio 2:Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.

# Calculamos o total de vendas para cada data de pedido
df_p2 = df.groupby('Data_Pedido')['Valor_Venda'].sum()

print(df_p2.head())


# Plot
plt.figure(figsize= (20,6))
df_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
plt.title('Total de Vendas por Data do pedido')
plt.show()