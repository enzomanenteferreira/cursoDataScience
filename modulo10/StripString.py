import pandas as pd

df = pd.read_csv('dataset.csv')

print(df['Data_Pedido'].head(3))

# Vamos remover os digitos 2 e 0 a esquerda do valor da variavel 'Data_Pedido'
print(df['Data_Pedido'].str.lstrip('20'))


#Substituindo os caracteres CG por AX na coluna 'ID_Cliente'
df['ID_Cliente'] = df['ID_Cliente'].str.replace('CG','AX')

print(df.head())