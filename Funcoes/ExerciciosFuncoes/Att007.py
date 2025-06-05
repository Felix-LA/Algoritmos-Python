# Crie uma função que receba um número e retorne True se ele for primo.

def calcularNumeroPar(num):
    if num % 2 != 0: print("True")
    if num % 3 != 0 and num % 2 != 0: print("True")
    if num % 5 != 0 and num % 2 != 0: print("True")
    if num % 7 != 0 and num % 2 != 0: print("True")
    else: print("False")

calcularNumeroPar(25)
