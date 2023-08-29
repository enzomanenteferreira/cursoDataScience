#projeto 1 - desenvolvimento de game em Python - versão 1

#import
import random
from os import system,name


#Função para limpar a tela a cada execução
def limpa_tela():
    #Windows
    if name == 'nt':
        _ = system('cls')
    #Mac ou Linux
    else:
        _ = system('clear')

#Função
def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #lista de palavras  para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'melancia']

    #escolher uma palavra randomicamente
    palavra = random.choice(palavras)

    #list comprehension - loop dentro da lista
    letras_palavras = ['_' for letra in palavra]

    #numero de chances 6
    chances = 6

    #lista para as letra erradas
    letras_erradas = []

    #loop enquanto o numero de chances for maior do que zero
    while chances > 0:
        #print
        print(" ".join(letras_palavras))
        print("\nChances restantes:", chances)
        print("letras erradas:", " ".join(letras_erradas))

        #Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_palavras[index] = letra
                index+=1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #condicional
        if "_" not in letras_palavras:
            print("\nVoce venceu, a palavra era:", palavra)
            break

    if "_" in letras_palavras:
        print("\nVoce perdeu, a palavra era:", palavra)


#bloco main
if __name__ == "__main__" :
    game()
    print("\nParabens. Voce está aprendendo programação em Python\n")