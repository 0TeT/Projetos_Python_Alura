import random
import string

tamanho_da_senha = 12
caracteres  = string.ascii_letters + string.digits + string.punctuation

lista_senha = random.choices(caracteres, k=tamanho_da_senha)

senha_final = ''.join(lista_senha)

print(f'Senha gerada: {senha_final}')