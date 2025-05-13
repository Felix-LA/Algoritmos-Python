quantidade = int(input("Informe a quantidade de Temperaturas a Adicionar: "))

temperatura = []
ano = []
mes = []

for count in range(quantidade):
    temperaturaAdicionar = float(input("Informe a Temperatura: "))
    mesAdicionar = int(input("Informe o Mes: "))
    anoAdicionar = int(input("Informe o Ano: "))

    temperatura.append(temperaturaAdicionar)
    mes.append(mesAdicionar)
    ano.append(anoAdicionar)


indexMaior = temperatura.index(max(temperatura))
indexMenor = temperatura.index(min(temperatura))

print(f"A maior temperatura foi {temperatura[indexMaior]} que ocorreu no mes {mes[indexMaior]} no Ano de {ano[indexMaior]}")
print(f"A menor temperatura foi {temperatura[indexMenor]} que ocorreu no mes {mes[indexMenor]} no Ano de {ano[indexMenor]}")


