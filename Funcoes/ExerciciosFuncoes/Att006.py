# Crie uma função que calcule o fatorial de um número (sem usar recursão).

def calculoFatorial(num):
    i = num - 1
    while i >= 1:
        num = num * i
        i = i - 1
    print(num)

calculoFatorial(6)
