# Crie uma função que retorne o menor valor entre três números.

def menorNumero(lista):
    return min(lista)

num1 = float(input("Digite o 1° Numero: "))
num2 = float(input("Digite o 2° Numero: "))
num3 = float(input("Digite o 3° Numero: "))

listaDeNumeros = [num1, num2, num3]

print(menorNumero(listaDeNumeros))