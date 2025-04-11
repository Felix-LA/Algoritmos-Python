salario = float(input("Informe o Valor do Salario: "))


if salario < 500.00: 
    reajuste = salario * 0.15
    salario = salario + reajuste
    print("O Novo salario é: ", salario)
    
elif salario > 500.00 and salario < 1000.00:
    reajuste = salario * 0.10
    salario = salario + reajuste 
    print("O Novo salario é: ", salario)

else:
    reajuste = salario * 0.05
    salario = salario + reajuste
    print("O Novo salario é: ", salario)