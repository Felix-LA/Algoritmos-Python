def calcularPagamento(qtdHoras, valorHora):
    horas = float(qtdHoras)
    taxa = float(valorHora)

    if horas <= 40:
        salario = horas * taxa
    else:
        horasExcedidas = horas - 40
        salario = 40 * taxa + (horasExcedidas * (1.5 * taxa))
    print(salario)
    # return salario

# calcularPagamento(42, 90)
# print(calcularPagamento(42, 90))
# print(calcularPagamento(42, 90) + 10)