# Crie uma função que receba uma lista e retorne a média dos elementos.

def MediaElementos(listaDeNumeros):
    somaDenumero = 0
    if len(listaDeNumeros) == 0:
        return 0
    
    for numero in listaDeNumeros:
        somaDenumero += numero

    media = somaDenumero / len(listaDeNumeros)

    return media

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(MediaElementos(lista))

