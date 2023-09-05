import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# Carregando o dataset
df = pd.read_csv('dataset.csv')

# Amostra dos dataset
#print(df.head())

#Pergunta de Negócio 10 :Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?Demonstre tudo através de um único gráfico.

# Agrupamos por categoria e subcategoria e calculamos a soma somenta para variaveis numericas
df_p10 = df.groupby(['Categoria',
                     'SubCategoria']).sum(numeric_only= True).sort_values('Valor_Venda',
                                                                          ascending= False).head(12)

# Convertemos a coluna valor_venda em numero inteiro e classificamos por categoria
df_p10 = df_p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()

# Criamos outro fataFrame somente com os totais por categoria
df_p10_cat = df_p10.groupby('Categoria').sum(numeric_only = True).reset_index()

# Dataframe com categorias
#print(df_p10_cat)

#Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

#Listas de cores para subcategoruas
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']


# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


#Plot

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Graficos das categorias
p1 = ax.pie(df_p10_cat['Valor_Venda'],
            radius = 1,
            labels = df_p10_cat['Categoria'],
            wedgeprops= dict(edgecolor = 'white'),
            colors = cores_categorias)

# Grafico das subcategorias
p2 = ax.pie(df_p10['Valor_Venda'],
            radius = 0.9,
            labels = df_p10['SubCategoria'],
            autopct = autopct_format(df_p10['Valor_Venda']),
            colors = cores_subcategorias,
            labeldistance= 0.7,
            wedgeprops= dict(edgecolor = 'white'),
            pctdistance= 0.53,
            rotatelabels= True)

# Limpa o centro do circulo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotaçoes
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de vendas: ' + '$ ' + str(int(sum(df_p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de vendas por categoria e top 12 subcategorias')
plt.show()