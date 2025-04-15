valorHora = float(input("Informe o valor da sua hora Trabalhada: "))
quantidadeHora = float(input("Informe a quantidade de horas trabalhadas: "))
salarioBruto = valorHora * quantidadeHora



if salarioBruto <= 900:
    descontoINSS = salarioBruto * 0.10
    fgts = salarioBruto * 0.11
    totalDesconto = descontoINSS
    salarioLiquido = salarioBruto - totalDesconto
    print(f"Salario Bruto: {salarioBruto}")
    print(f"Imposto de Renda: ISENTO ")
    print(f"INSS: {descontoINSS}")
    print(f"FGTS: {fgts}")
    print(f"Total de Descontos: {totalDesconto}")
    print(f"Salario Liquido: {salarioLiquido}")

elif salarioBruto > 900 and salarioBruto <= 1500:
    impostoDeRenda = salarioBruto * 0.05
    descontoINSS = salarioBruto * 0.10
    fgts = salarioBruto * 0.11
    totalDesconto = descontoINSS + impostoDeRenda
    salarioLiquido = salarioBruto - totalDesconto
    print(f"Salario Bruto: {salarioBruto}")
    print(f"Imposto de Renda: {impostoDeRenda}")
    print(f"INSS: {descontoINSS}")
    print(f"FGTS: {fgts}")
    print(f"Total de Descontos: {totalDesconto}")
    print(f"Salario Liquido: {salarioLiquido}")

elif salarioBruto > 1500 and salarioBruto <= 2500:
    impostoDeRenda = salarioBruto * 0.10
    descontoINSS = salarioBruto * 0.10
    fgts = salarioBruto * 0.11
    totalDesconto = descontoINSS + impostoDeRenda
    salarioLiquido = salarioBruto - totalDesconto
    print(f"Salario Bruto: {salarioBruto}")
    print(f"Imposto de Renda: {impostoDeRenda}")
    print(f"INSS: {descontoINSS}")
    print(f"FGTS: {fgts}")
    print(f"Total de Descontos: {totalDesconto}")
    print(f"Salario Liquido: {salarioLiquido}")

else:
    impostoDeRenda = salarioBruto * 0.20
    descontoINSS = salarioBruto * 0.10
    fgts = salarioBruto * 0.11
    totalDesconto = descontoINSS + impostoDeRenda
    salarioLiquido = salarioBruto - totalDesconto
    print(f"Salario Bruto: {salarioBruto}")
    print(f"Imposto de Renda: {impostoDeRenda}")
    print(f"INSS: {descontoINSS}")
    print(f"FGTS: {fgts}")
    print(f"Total de Descontos: {totalDesconto}")
    print(f"Salario Liquido: {salarioLiquido}")