import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# carrega o dataset
df = pd.read_csv('dataset.csv')

#print(df.head())

# Verificar se alguma coluna tem valores vazios
#print(df.isnull().sum())

# Resumo estatistico da variavel alvo
df['valor_aluguel'].describe()

# Histograma da variavel alvo
#sns.histplot(data = df, x = 'valor_aluguel', kde = True)
#plt.show()

# Correlação entre as variaveis
#print(df.corr())

# analisando a relação entre a variavel de entrada area_m2 e a variavel alvo valor_aluguel
sns.scatterplot(data = df, x = "area_m2", y = "valor_aluguel")
plt.show()
