import matplotlib as mpl
# O matplotlib.pyplot é uma coleção de funçoes e estilos do Matplotlib
import matplotlib.pyplot as plt

# O método plot() define os eixos do gráfico
plt.plot([1,3,5], [2,4,7])
#plt.show()

x = [2,3,5]
y = [3,5,7]

#plt.plot(x,y)
#plt.xlabel('Variavel 1')
#plt.ylabel('Variavel 2')
#plt.title('Teste Plot')
#plt.show()


# Gráfico de barras

x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]

#plt.bar(x1,y1,label = 'Barras', color = 'black')
#plt.legend()
#plt.show()

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

#plt.bar(x1,y1, label = 'Listas1', color = 'blue')
#plt.bar(x2,y2, label = 'Listas2', color = 'red')
#plt.legend()
#plt.show()

idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]

ids = [x for x in range(len(idades))]
print(ids)

plt.bar(ids,idades)
#plt.show()

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(idades, bins, histtype= 'bar', rwidth = 0.8)
plt.show()

plt.hist(idades,bins,histtype = 'stepfilled', rwidth = 0.8)
plt.show()