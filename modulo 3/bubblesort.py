# bubble sort, funciona comparando cada elemento com o proximo, trocando-os de lugar se estiverem em ordem incorreta

lista = [2,4,10,3,6,23,100,76,25,89,33,45]


def bubble_sort(arr):

    n = len(arr) #tamanho do array

    #loop para cada elemento i do array
    for i in range(n):

        #loop para cada elemento j do array
        for j in range(0,n-i-1):

            #se o elemento i for maior que o elemento j
                if arr[j] > arr[j+1]:

                     #troca os elementos i e j
                     arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(lista))