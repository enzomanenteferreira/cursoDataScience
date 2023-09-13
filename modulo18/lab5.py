
# Problema de negocio:
# Construir um robo(modelo em Python) baseado em inteligencia artificial que aprenda a operar na bolsa de valores a partir de experimentos
# de compra e venda de açoes, dado um saldo inicial o modelo deve apresentar o resultado (lucro) a ser obtido depois de açoes de compra e venda

import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

# carrega os dados
df = pd.read_csv('dataset.csv')

print(df.head())


# candlestick
fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                open = df['AAPL.Open'],
                high = df['AAPL.High'],
                low = df['AAPL.Low'],
                close = df['AAPL.Close'])])

fig.show()

# Vamos trabalhar com a cotação de fechamento da ação da Apple
precos = df['AAPL.Close'].values


# configurando o algoritmo Q-Learning
print('\nDefinindo os Hiperparametros do Q-Learning...')
num_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

# configuração do ambiente de negociação
print('\nConfigurando o ambiente de Negociação...')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

# Funcao para executar uma ação e retornar a recompensa e o proximo estado
def executar_acao(estado, acao, saldo, num_acoes, preco):

    # ação de comprar 
    if acao == 0:
        if saldo >= preco:
            num_acoes +=1
            saldo -= preco
    
    # acao de vender
    elif acao == 1:
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco
    
    # define o lucro
    lucro = saldo + num_acoes * preco - saldo_inicial
    return(saldo, num_acoes, lucro)


# treinamento do robô
print('\nInicializando a Tabela Q...')
q_tabela = np.zeros((len(precos), len(acoes)))


# Treinamento
print('\nInicializando o Treinamento...')
for _ in range(num_episodios):

    #Define o saldo
    saldo = saldo_inicial

    #Define o numero de açoes
    num_acoes = num_acoes_inicial

    #loop
    for i, preco in enumerate(precos[:-1]):
        estado = i

        # escolher a ação usando a politica epsilon-greedy
        if np.random.random() < epsilon:
            acao = np.random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])

        # Executar a acao e obter a recompensa e o proximo estado
        saldo,num_acoes,lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i+1

        # Atualizar a tabela Q
        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

print('\nTreinamento Concluido...')

# executando o robô trading e prevendo o lucro de operaçãoes na bolsa de valores
# valores iniciais para testar o agente
saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o Agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)

print('\nExecução Concluida...')

print('numero de acoes: ', num_acoes)

# vendendo todas as açoes no ultimo preço
saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro,2)
print(f"\nComeçamos a negociação com saldo inicial de 1000 e tivemos lucro de: {lucro_final}")