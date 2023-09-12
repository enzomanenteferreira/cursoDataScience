
# Problema de negocio:
# construir um modelo de inteligencia artificial capaz de classificar imagens considerando 10 categorias['airplane', 'automobile','cat','deer','dog','horse,'frog','ship','truck']
# dada uma nova imagem de uma dessas categorias o modelo deve ser capaz de classificar e indicar o que é a imagem

import tensorflow as tf
import keras.datasets.cifar10 as cifar10
from keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


#https://www.cs.toronto.edu/~kriz/cifar.html
# carrega o dataset CIFAR-10
(imagens_treino, labels_treino), (imagens_teste, labels_teste) = cifar10.load_data()

# Classes das imagens
nomes_classes = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

# normaliza os valores dos pixels para que os dados fiquem na mesma escala
imagens_treino = imagens_treino / 255.0
imagens_teste = imagens_teste / 255.0

# funcao para exibir as imagens
def visualiza_imagens(images,labels):
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap = plt.cm.binary)
        plt.xlabel(nomes_classes[labels[i][0]])
    #plt.show()


# executa a função
visualiza_imagens(imagens_treino, labels_treino)


# Modelo

# cria o objeto de sequencia de camadas
modelo = models.Sequential()

# Adiciona o primeiro bloco de convulação e max pooling(camada de entrada)
modelo.add(layers.Conv2D(32,(3,3), activation= 'relu', input_shape = (32,32,3)))
modelo.add(layers.MaxPooling2D((2,2)))

# Adiciona o segundo bloco de convolução e max pooling (camada intermediaria)
modelo.add(layers.Conv2D(64,(3,3), activation = 'relu'))
modelo.add(layers.MaxPooling2D((2,2)))

# Adiciona o terceiro bloco de convolução e max pooling (camada intermedaria)
modelo.add(layers.Conv2D(64,(3,3), activation= 'relu'))
modelo.add(layers.MaxPooling2D((2,2)))

# adicionar camadas de classificação
modelo.add(layers.Flatten())
modelo.add(layers.Dense(64, activation='relu'))
modelo.add(layers.Dense(10, activation ='softmax'))

# sumário do modelo
print(modelo.summary())

# compilaçao do modelo
modelo.compile(optimizer= 'adam', 
               loss = 'sparse_categorical_crossentropy',
               metrics = ['accuracy'])

history = modelo.fit(imagens_treino,
                     labels_treino,
                     epochs= 10,
                     validation_data=(imagens_teste,labels_teste))


# avalia o modelo
erro_teste, acc_teste = modelo.evaluate(imagens_teste, labels_teste, verbose=2)
print('\nAcuracia com Dados de Teste:', acc_teste)

# Deploy do Modelo

# Carrega uma nova imagem
nova_imagem = Image.open("nova_imagem.jpg")

# dimensão da imagem (em pixels)
nova_imagem.size

#obtem largura e altura da imagem
largura = nova_imagem.width
altura = nova_imagem.height
print("A largura da imagem eh: ", largura)
print("A altura da imagem eh: ", altura)

#Redimensiona para 32x32 pixels
nova_imagem = nova_imagem.resize((32,32))

# Exibir a imagem
plt.figure(figsize=(1,1))
plt.imshow(nova_imagem)
plt.xticks([])
plt.yticks([])
plt.show()

# Converte a imagem para um array NumPy e normaliza
nova_imagem_array = np.array(nova_imagem) /255.0

#expande a dimensão do array para que ele tenha o formato(1,32,32,3)
nova_imagem_array = np.expand_dims(nova_imagem_array,axis =0)

# Previsões
previsoes = modelo.predict(nova_imagem_array)
print(previsoes)

# obtem a classe com maior probabilidade e o nome da classe
classe_prevista = np.argmax(previsoes)
nome_classe_prevista = nomes_classes[classe_prevista]

print("A nova imagem foi classificada como:", nome_classe_prevista)