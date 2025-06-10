# Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.

def maioresValores(valores, quantidade):
    valoresOrdenados = sorted(valores, reverse=True)
    return valoresOrdenados[ : quantidade]

teste = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(maioresValores(teste, 5))