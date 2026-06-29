import os
import random

# print(numero_sorteado)
def jogo():
    '''Jogo de adivinhação'''

    numero_secreto = random.randint(1,100)
    tentativas = 0

    while True:
        try:
            jogada = int(input('Tente adivinhar o número (1-100): '))

            if jogada > 100 or jogada < 1:
                os.system('clear')
                raise ValueError('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.\n')
            
            tentativas += 1

            if jogada == numero_secreto:
                os.system('clear')
                print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.\n')
                break
            elif jogada > numero_secreto:
                os.system('clear')
                print(f'Muito alto! Tente novamente: {jogada}\n')
            else:
                os.system('clear')  
                print(f'Muito baixo! Tente novamente: {jogada}\n')

        except ValueError as e:
            os.system('clear')  
            print(f'Entrada inválida: {e}\n')
    return

jogo()
