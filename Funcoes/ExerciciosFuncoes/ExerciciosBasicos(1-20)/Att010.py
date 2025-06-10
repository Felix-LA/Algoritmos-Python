# Escreva uma função que conte quantas vogais há em uma string.

def contarVogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return print(contador)

contarVogais("sfldjkeo")