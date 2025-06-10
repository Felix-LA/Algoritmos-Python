# Escreva uma função que identifique o segundo maior número em uma lista.

def segundoMaiorNumero(listaDeNumeros):
    maiorNumero = max(listaDeNumeros)
    listaDeNumeros.remove(maiorNumero)
    maiorNumero = max(listaDeNumeros)
    return print(maiorNumero)

teste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

segundoMaiorNumero(teste)