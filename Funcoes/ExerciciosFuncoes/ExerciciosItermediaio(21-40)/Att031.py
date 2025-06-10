# Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        return print("Faça direito")

print(calculadora(2,2,"+"))
print(calculadora(2,2,"-"))
print(calculadora(2,2,"*"))
print(calculadora(2,2,"/"))
print(calculadora(2,2,"**"))