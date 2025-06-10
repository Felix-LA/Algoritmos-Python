# Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).

def tabuada(numero):
    index = 1
    for index in range(1, 11):
        resultado = numero * index
        print(f"{numero} * {index}: {resultado}")

tabuada(5)