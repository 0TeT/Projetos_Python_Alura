import random
import os

def regra_jogo(jogada, maquina):
    
    if jogada == maquina :
            mensagem = 'Empate!' 
    elif ( 
        (jogada == "pedra" and maquina == "tesoura") or 
        (jogada == "papel" and maquina == "pedra") or 
        (jogada == "tesoura" and maquina == "papel") 
    ): 
       mensagem = 'Você venceu!' 
    else:
        mensagem = 'Você Perdeu!'
    return mensagem

def jogadas():
    lista_jogadas = ['pedra', 'papel', 'tesoura']

    while True:
        try:
            jogador = input('Escolha - Pedra, Papel, Tesoura (ou "sair"): ').lower().strip()
            
            if jogador == 'sair':
                print("Obrigado por jogar!")
                break
                
            if jogador not in lista_jogadas:
                os.system('clear')
                print('Erro: Opção inválida. Tente novamente.\n')
                continue # Volta para o início do loop
            
            maquina = random.choice(lista_jogadas)
            
            os.system('clear')
            print(f"Você escolheu: {jogador}")
            print(f"A máquina escolheu: {maquina}")
            print("-" * 30)
            print(f'{regra_jogo(jogador, maquina)}\n')
            
        except Exception as e:
            os.system('clear')
            print(f'Ocorreu um erro inesperado: {e}\n')
jogadas()