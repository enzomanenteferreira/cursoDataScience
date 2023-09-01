import pandas as pd

df = pd.read_csv('dataset.csv')

# Concatenando String
df['Pedido_Segmento'] = df['ID_Pedido'].str.cat(df['Segmento'], sep = '-')

print(df.head())