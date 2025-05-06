nomeUsuario = []
cpf = []
rg = []
telefone = []
numeroDaAgencia = []
numeroDaConta = []
saldo = []

while True:
    print()
    print("-----Bem-Vindo!!!-----")

    print('0 - Cadastrar Usuario: ')
    print("1 - Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    acao = input("Informe o que deseja fazer: ")
    print()

    if acao == '0':
        novoUsuarioNome = input("Informe o Nome do Usuario: ")
        novoUsuarioCpf = input("Informe o CPF do Usuario: ")
        novoUsuarioRG = input("Informe o Rg do Usuario: ")
        novoUsuarioTelefone = int(input("Informe o Telefone: "))
        novoUsuarioNumeroDaAgencia = int(input("Informe o numero da Agencia: "))
        novoUsuarioNumeroDaConta = int(input("Informe o numero da Conta: "))
        novoUsuarioSaldo = float(input("Informe o Saldo: "))

        nomeUsuario.append(novoUsuarioNome)
        cpf.append(novoUsuarioCpf)
        rg.append(novoUsuarioRG)
        telefone.append(novoUsuarioTelefone)
        numeroDaAgencia.append(novoUsuarioNumeroDaAgencia)
        numeroDaConta.append(novoUsuarioNumeroDaConta)
        saldo.append(novoUsuarioSaldo)
    
    elif acao == '1':
        nomeConsulta = input("Informe o Nome da Conta: ")
        if nomeConsulta in nomeUsuario:
            index = nomeUsuario.index(nomeConsulta)
            print(f"O saldo de {nomeConsulta} é {saldo[index]:.2f}")
        else: print("Usuario nao encontrado")
    
    elif acao == '2':
        nomeConsulta = input("Informe o Nome da Conta: ")
        if nomeConsulta in nomeUsuario:
            index = nomeUsuario.index(nomeConsulta)
            deposito = float(input("Informe o saldo a ser depositado: "))
            saldo[index] += deposito
            print("Saldo Depositado")

        else: print("Usuario nao encontrado")
    
    elif acao == '3':
        nomeConsulta = input("Informe o Nome da Conta: ")
        if nomeConsulta in nomeUsuario:
            index = nomeUsuario.index(nomeConsulta)
            saque = float(input("Informe o saldo a ser sacado: "))
            if saldo[index] > saque:
                saldo[index] -= saque
                print("Saldo Depositado")
            else: print("Saldo Insuficiente")

        else: print("Usuario nao encontrado")

    elif acao == '4':
        print("Ate Mais!!!")
        break

    else: print("Faça uma ação valida")
