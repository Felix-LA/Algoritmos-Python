# Crie uma função que receba um número e retorne uma lista com todos os divisores dele.

def encontrarDivisores(numero):
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    return divisores

print(encontrarDivisores(30))