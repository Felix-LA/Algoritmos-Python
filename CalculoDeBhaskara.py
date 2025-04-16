import math

a = int(input("Informe o Primeiro Numero: "))
b = int(input("Informe o Segundo Numero: "))
c = int(input("Informe o Terceiro Numero: "))

resultadoA = ((-b) + (math.sqrt((b * b) - 4 * a * c))) / (2 * a)
resultadoB = ((-b) - (math.sqrt((b * b) - 4 * a * c))) / (2 * a)

print(resultadoA)
print(resultadoB)