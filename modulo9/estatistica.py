import numpy as np

#criando um array
arr = np.array([15,23,63,94,75])

#calcular a media do array
print(np.mean(arr))

#desvio padrao (standard deviation)
print(np.std(arr))

#variância - é uma medida util para avaliar a variabilidade dos dados em torno da media
#se a variância for baixa, isso indica que os valores estão proximos da media e tem pouca variabilidade
#se a variância for alta, isso indica que os valores estão distantes da media e tem alta variabilidade
print(np.var(arr))