Clientes = {}
Passagens = {}
Avioes = {}
Tripulocao = {}

while True:
    print("------------MENU------------")
    print("0 - Relatorio")
    print("1 - Cadastro Cliente")
    print("2 - Cadastro Passagem")
    print("3 - Cadastro Aviao")
    print("4 - Cadastro Tripulação")
    print("5 - Sair")
    try:
        acao = int(input("Informe o que deseja fazer: "))
    except ValueError:
        print("Informe uma ação valida")

    if acao == '0':
        print("------------MENU RELATORIOS------------")
        print("0 - Relatorio de Clientes")
        print("1 - Relatorio de Passagens")
        print("2 - Relatorio de Aviões")
        print("3 - Relatorio de Tripulação")
        print("4 - Voltar")
        try:
            acaoRelatorio = int(input("Informe o que deseja fazer: "))
        except:
            print("Informe uma ação valida")
        if acaoRelatorio == '0': print(Clientes)
        elif acaoRelatorio == '1': print(Passagens)
        elif acaoRelatorio == '2': print(Avioes)
        elif acaoRelatorio == '3': print(Tripulocao)
        elif acaoRelatorio == '4': continue
        else: print("Informe uma ação Valida")

    elif acao == '1':
        
        nome = input("Informe o Nome: ")
        sobreNome = input("Informe o Sobrenome: ")
        cpf = input("Informe o CPF: ")
        
        try:
            rg = int(input("Informe o Rg: "))
            endereco = input("Informe o Endereço: ")
            fone = int(input("Informe o Telefone: "))
            idade = int(input("Informe a Idade: "))
        except:
            print("Informe um Valor Numerico: ")
        Clientes [cpf] =  {'Nome ' : nome, 'SobreNome ' : sobreNome, 'Rg' : rg, 'CPF' : cpf, 
                           'Endereço' : endereco, 'Telefone' : fone, 'idade' : idade}

        
    elif acao == '2':
        destino = input("Informe o Destino do Voo: ")
        origem = input("Informe a Origem do Voo")
        duracao = int(input("Informe a duração do Voo(em Minutos): "))
        valorPassagem = float(input("Informe o Valor da Passagem: "))
        desconto = valorPassagem * 0.05

        Passagens [origem, destino] = {'Origem' : origem, 'Destino' : destino, 'Duração' : duracao, 
                                       'ValorDePasagem' : valorPassagem, 'Desconto' : desconto}
        
    elif acao  == '3':
        modelo = input("Informe o Modelo do Aviao: ")
        cor = input("Informe a Cor do Aviao: ")
        try:
            ano = int(input("Informe o Ano de Fabricação do Aviao: "))
            horasDeVoo = int(input("Informe as Horas de Voo do aviao: "))
            quantidadeDePassageiros = int(input("Informe a quantidade da Capacidade de Passageiros: "))
        except ValueError:
            print("Informe valor Numerico: ")
        
        Avioes [modelo, cor, ano] = {'Modelo' : modelo, 'Ano' : ano, 'Cor' : cor, 'HorasDeVoo' : horasDeVoo,
                                     'QuantidadeDePassageiros' : quantidadeDePassageiros}
        
    elif acao == '4':
        nome = input("Informe o Nome do Tripulante: ")
        cargo = input("Informe o Cargo do Tripulante: ")
        dataDeAdmissao = input("Informe a data de Admissao: ")

        try:
            idade = int(input("Informe a Idade do Tripulante: "))
            fone = int(input("Informe o Telefone do Tripulante: "))
        except:
            print("Informe valor Numerico: ")
        
        Tripulocao [nome, cargo] = {'Nome' : nome, 'Cargo' : cargo, 'Idade' : idade,
                                    'Data de Admissao' : dataDeAdmissao, 'Telefone' : fone}
        
    elif acao == '5':
        print("Bye - Bye")
        break
     
    else: print("Digite uma ação Valida")
