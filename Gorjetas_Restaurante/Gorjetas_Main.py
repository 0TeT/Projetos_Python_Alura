import os

def calculo_gorjeta(conta,porcentagem_gorjeta):
    '''Função para calcular a porcentagem da gorjeta'''

    valor_gorjeta = conta*(porcentagem_gorjeta/100)
    return valor_gorjeta

def total_da_conta(conta,gorjeta):
    ''' Função para calcular o valor total da conta'''

    valor_total = conta + gorjeta
    return valor_total


def exibir_valor_conta(valor_conta,porcentual_gorjeta):
    '''Função para Exibir e formatar as saidas
        algo parecido como uma nota fiscal
    '''

    os.system('clear')
    # essa variavel esta recebendo a saida da função calculo_gorjeta()
    valor_da_gorjeta = calculo_gorjeta(valor_conta,porcentual_gorjeta)

    print('--'*16)
    print('\033[1mNota Fiscal\033[1m\n' )
    print(f'Valor da Conta: R$ {valor_conta:.2f}')
    print(f'Percentual da Gorjeta: {porcentual_gorjeta:.2f}%')
    print(f'Valor Gorjeta: R$ {valor_da_gorjeta:.2f}')
    print('--'*16)
    print(f'Valor Total da Conta: R$ {total_da_conta(valor_conta, valor_da_gorjeta):.2f}')
    print('--'*16)


try:
    valor_conta = float(input('Digite o valor da conta: R$ ').replace(',','.'))
    porcentagem = float(input('Digite o valor da gorjeta: ').replace(',','.'))

    exibir_valor_conta(valor_conta, porcentagem)
except Exception as e:
    print('Erro: Informar Apenas Numeros!')

