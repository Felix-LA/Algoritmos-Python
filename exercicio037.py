# quantidade = int(input("Informe quantas Idade irá Cadastrar: "))
# media = 0
# for cont in range(quantidade):
#     idade = int(input("Informe a Idade: "))
#     media += idade
    
# media = media / quantidade
# if media >= 0 and media < 25: print(f"A media de Idade é: {media}"), print("A turma é Jovem")
# elif media >= 25 and media < 60: print(f"A media de Idade é: {media}"), print("A turma é Adulta")
# else: print(f"A media de Idade é: {media}"), print("A turma é VELHA!!!")

somaIdade = 0
count = 0
media = 0
verificaçãoResposta = ['SIM', 'S']
while True:

    verificação = input("Deseja adicionar uma Idade? ").upper()

    if verificação not in verificaçãoResposta and somaIdade == 0:
        print("Adicione uma Idade")
    elif verificação == 'SIM' or verificação == 'S':
        idade = int(input("Informe a Idade: "))
        somaIdade += idade
        count += 1
    else:
        media = somaIdade / count
        if media >= 0 and media < 25: print(f"A media de Idade é: {media:.2f}"), print("A turma é Jovem")
        elif media >= 25 and media < 60: print(f"A media de Idade é: {media:.2f}"), print("A turma é Adulta")
        else: print(f"A media de Idade é: {media:.2f}"), print("A turma é VELHA!!!")
        break
        