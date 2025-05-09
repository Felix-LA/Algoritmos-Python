# num1 = int(input("Informe um Numero: "))
# num2 = int(input("Informe um Numero: "))
# soma = 0

# if num1 < num2:
#     for count in range(num1,num2):
#         soma += count
# else:
#     for count in range(num2,num1):
#         soma += count



# print("O maior Numero é: ", num2)
# print("O menor Numero é: ", num1)
# print("A soma dos Numeros é: ", soma)

quantidade = int(input("Informe a quantidade de numeros: "))

maior = float('-inf')
# maior = 0

menor = float('inf')
# menor = 99999999999

soma = 0

for count in range(quantidade):
    numero = int(input("Informe um numero: "))
    if numero > maior: maior = numero
    if numero < menor: menor = numero
    soma += numero

print("O maior Numero é: ", maior)
print("O menor Numero é: ", menor)
print("A soma dos Numeros é: ", soma)
