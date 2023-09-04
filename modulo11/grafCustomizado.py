# O pylab combina funcionalidades do pyplot com funcionalidades do numpy
from pylab import *


# Gráfico de linha
 
# Dados
x = linspace(0,5,10)
y = x ** 2

#cria a figura
fig = plt.figure()

# define a escala dos eixos
axes = fig.add_axes([0,0,0.8,0.8])

#cria o plot
axes.plot(x,y,'r')

#Labels e titulo
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Grafico de linha')
plt.show()