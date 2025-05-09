num1 = int(input("Informe um Numero: "))
num2 = int(input("Informe um Numero: "))
soma = 0
if num1 < num2:
    for i in range(num1 + 1, num2): 
        print(i)
        soma += i
    print(soma)
else:
    for i in range(num2 + 1, num1):
        print(i)
        soma += i
    print(soma)

