while True:
    print("Bem-Vindo")
    print("X-Sair")
    print("A-Adição")
    print("S-Subtração")
    print("M-Multiplicação")
    print("D-Divisão")

    operacao = input("Informe a Operação Desejada: ").upper()

    if operacao == 'A':
        valor1 = int(input("Informe o Primeiro Valor: "))
        valor2 = int(input("Informe o segundo Valor: "))
        resultado = valor1 + valor2
        print(f"O resultado da adição de {valor1} e { valor2} é {resultado}")
    
    elif operacao == 'S':
        valor1 = int(input("Informe o Primeiro Valor: "))
        valor2 = int(input("Informe o segundo Valor: "))
        resultado = valor1 - valor2
        print(f"O resultado da subtração de {valor1} e {valor2} é {resultado}")

    elif operacao == 'M':
        valor1 = int(input("Informe o Primeiro Valor: "))
        valor2 = int(input("Informe o segundo Valor: "))
        resultado = valor1 * valor2
        print(f"O resultado da multiplicação de {valor1} e {valor2} é {resultado}")

    elif operacao == 'D':
        valor1 = int(input("Informe o Primeiro Valor: "))
        valor2 = int(input("Informe o segundo Valor: "))
        resultado = valor1 / valor2
        print(f"O resultado da divisão de {valor1} e {valor2} é {resultado}")

    elif operacao == 'X':
        print("Volte Sempre")
        break

    else: print("Digite uma operação valida")
