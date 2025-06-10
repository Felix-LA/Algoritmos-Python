# Crie uma função que receba um número e retorne True se ele for primo.

def calcularNumeroPar(num):
    if num % 2 == 1 or num == 2: print("True")
    elif num % 3 == 1 and num % 2 != 0 or num == 3: print("True")
    elif num % 5 == 1 and num % 2 != 0 or num == 5: print("True")
    elif num % 7 == 1 and num % 2 != 0 or num == 7: print("True")
    else: print("False")

calcularNumeroPar(20)

# def primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(primo(23))