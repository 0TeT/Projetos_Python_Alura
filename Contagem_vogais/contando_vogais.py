def contando_vogais(texto):
    ''' Função que conta quantas vogais tem no texto '''

    vogais = ['a','e','i','o','u']
    total = 0
    try:
        for letra in texto:
            if letra in vogais:
                total += 1
        return total
    except Exception as e:
        return e     

texto = input('Digite um texto: ').lower()
quantidade = contando_vogais(texto)

print(f'O texto contém {quantidade} vogais.')