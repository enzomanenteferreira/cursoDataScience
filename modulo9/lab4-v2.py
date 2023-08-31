#Hangman Game
#Programação orientada a objetos
#Imports
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    #windows
    if name == 'nt':
        _= system('cls')

    #Mac ou linux
    else:
        _= system('clear')

#Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#classe
class Hangman:
    #metodo construtor
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []
    
    #metodo para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False
        
        return True
    
    #metodo para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
    
    #metodo para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False
    
    #metodo para nao mostrar a letra no board
    def hide_palavra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    
    #metodo para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        
        print(board[len(self.letras_erradas)])

        print('\nPalavra: ' + self.hide_palavra())

        print('\nLetras erradas: ',)

        for letra in self.letras_erradas:
            print(letra,)

        print()

#metodo para ler uma palavra de forma aleatoria do banco de dados
def rand_palavra():
    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    return palavra

#metodo main - execução do programa
def main():
    limpa_tela()

    #cria o objeto e seleciona uma palavra randomicamento
    game = Hangman(rand_palavra())

    #enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        # Status do game
        game.print_game_status()

        # recebe um input do terminal
        user_input = input('\nDigite uma letra: ')

        #Verifica se a letra digitado faz parte da palavra
        game.guess(user_input)

        #verifica o status do jogo
        game.print_game_status()

    #de acordo com o status, imprime mensagem na tela para o usuario
    if game.hangman_won():
        print('\nParabens! Voce venceu!!')

    else:
        print('\nGame over! Voce Perdeu.')
        print('A palavra era ' + game.palavra)

#executa o programa
if __name__  == "__main__":
    main()