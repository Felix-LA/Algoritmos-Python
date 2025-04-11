salario = float(input("Informe o salario: "))

if salario <= 280.55:
    salarioAntigo = salario
    reajuste = salario * 0.2251
    salario = salario + reajuste
    print("O salario antigo é: {0:.2f}" .format(salarioAntigo))
    print("O porcentual de ajuste será de: 0.2251")
    print("O reajuste sera de: {0:.2f}" .format(reajuste))
    print("O novo salario é: {0:.2f}" .format(salario))

elif salario > 280.56 and salario <= 709.72:
    salarioAntigo = salario
    reajuste = salario * 0.1539
    salario = salario + reajuste
    print("O salario antigo é: {0:.2f}" .format(salarioAntigo))
    print("O porcentual de ajuste será de: 0.1539")
    print("O reajuste sera de: {0:.2f}" .format(reajuste))
    print("O novo salario é: {0:.2f}" .format(salario))

elif salario > 709.72 and salario <= 1501.33:
    salarioAntigo = salario
    reajuste = salario * 0.1097
    salario = salario + reajuste
    print("O salario antigo é : {0:.2f}" .format(salarioAntigo))
    print("O porcentual de ajuste será de: 0.1097")
    print("O reajuste sera de: {0:.2f}" .format(reajuste))
    print("O novo salario é: {0:.2f}" .format(salario))

elif salario >= 1501.34:
    salarioAntigo = salario
    reajuste = salario * 0.0519
    salario = salario + reajuste
    print("O salario antigo é: {0:.2f}" .format(salarioAntigo))
    print("O porcentual de ajuste será de: 0.0519")
    print("O reajuste sera de: {0:.2f}" .format(reajuste))
    print("O novo salario é: {0:.2f}" .format(salario))