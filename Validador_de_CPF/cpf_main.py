import re

def validar_cpf(cpf):
    ''' Função para Validar de os numeros passados tem as quantidades corretas '''

    if len(cpf) == 11:
        return print('CPF Válido')
    else:
        return print('Erro: O CPF deve ter exatamente 11 dígitos.!')
    
def validar_numero(cpf_num):
    ''' Função para Identificar se á caracteres  '''

    try:
        cpf_limpo = re.sub(r'[,.-]','',cpf_num)
        int(cpf_limpo)
        return validar_cpf(cpf_limpo)
    except:
        return print('Erro: O CPF deve ter apenas números. ')


cpf = str(input("Digite seu CPF: "))
validar_numero(cpf)

# Dica do professor é ao inves de criar uma função para validar poderia ser usado a função isdigit()