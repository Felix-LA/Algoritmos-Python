numeroFatoracao = int(input("Informe o Numero a ser Fatorado: "))
resultadoFatoracao = 1

for count in range(numeroFatoracao, 1, -1):
    resultadoFatoracao *= count

print(resultadoFatoracao)
