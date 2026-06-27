import os

def conferindo_palavra(texto):
    palavras_longas = []
    for palavra in texto:
        if len(palavra) >= 10:
            palavras_longas.append(palavra)
    return list(palavras_longas)


texto = input('Digite um texto: ').replace('.', ' ').split()

palavra_longa = conferindo_palavra(texto)


if len(palavra_longa) == 0:
    os.system('clear')
    print('Nenhuma palavra longa foi encontrada no texto.\n')
else:
    os.system('clear')
    print('Palavras longas encontradas: ', *palavra_longa, sep=', ')

    