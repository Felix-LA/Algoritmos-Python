# Crie uma função que gere uma lista com os n primeiros números pares.

def gerarListaDeNumerosPares(QuantidadeDeNumerosPares):
    pares = []
    numero = 0

    while len(pares) < QuantidadeDeNumerosPares:
        if numero % 2 == 0:
            pares.append(numero)
        numero += 1

    return pares

print(gerarListaDeNumerosPares(7))