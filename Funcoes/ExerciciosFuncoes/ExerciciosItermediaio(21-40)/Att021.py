# Crie uma função que receba uma lista de números e retorne uma nova lista com os números elevados ao quadrado.

def elevandoNumerosAoQuadrado(listaDeNumeros):
    numerosAoQuadrado = []

    for numero in listaDeNumeros:
        numerosAoQuadrado.append(numero ** 2)

    return numerosAoQuadrado

teste = [1, 2, 3, 4, 5]
print(elevandoNumerosAoQuadrado(teste))