import os

def calculos(numero1, numero2, operacao):
    ''' Função para realizar os calculos'''

    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2
    else:
        raise ValueError('Operação inválida!')
    

try:
    primeiro_numero = float(input('Digite o primeiro número: '))
    operacao = input('Escolha a operação (+,-,*,/): ').strip()
    segundo_numero = float(input('Digite o segundo número: '))

    resultado = calculos(primeiro_numero, segundo_numero,operacao)
 
    os.system('clear')
    print(f'Resultado: {round(resultado,2)}\n')

except ValueError as e:
    os.system('clear')
    
    if str(e).startswith('Operação'):
        print(f'Erro: {e}')
    else:
        print(f'Erro: Entrada inválida. Digite apenas números.\n')

except ZeroDivisionError:
    os.system('clear')
    print('Erro: Divisão por zero não é permitida.\n')
