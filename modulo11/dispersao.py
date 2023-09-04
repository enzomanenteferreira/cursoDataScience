import matplotlib as mpl
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]

plt.scatter(x,y,label = 'Pontos', color = 'black', marker = 'x')
plt.legend()
plt.show()

# Grafico de pizza
fatias = [7,2,2,13]

atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode=(0,0.2,0,0))
plt.show()