while True:

    nome = input("Informe o nome: ")
    idade = int(input("Informe a sua Idade: "))
    salario = float(input("Informe o Salario: "))
    sexo = input("Informe o Sexo(F - Feminino / M - Masculino / O - Outros): ").upper()
    estadoCivil = input("Informe o seu estado Civil (S-Solteiro / C-Casado / V-Viuvo / D-Divorsiado): ").upper()
    respostasSexos = ["S", "M", "O"]
    RespostasEstadocivil = ["S", "C", "V", "D"]
    Validation = True

    if len(nome) <= 3: 
        print("Informe um nome com mais caracters") 
        Validation = False
    elif  0 < idade > 150: 
        print("Informe uma Idade entre 0 e 150")
        Validation = False
    elif salario <= 0: 
        print("Informe Um salario maior que 0")
        Validation = False
    elif sexo not in respostasSexos: 
        print("Informe um sexo adequado")
        Validation = False
    elif estadoCivil not in RespostasEstadocivil: 
        print("informe um estado civil valido")
        Validation = False

    if Validation:
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Salario: ", salario)
        print("Sexo: ", sexo)
        print("Estado Civil: ", estadoCivil)
        break
    else: 
        pass