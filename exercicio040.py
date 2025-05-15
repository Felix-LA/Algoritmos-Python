estoque = {'banana' : 20, 'maca': 3, 'caneta': 0}

while True:
    print("-----MENU-----")
    print("0 - Adicionar Produto")
    print("1 - Consultar Produto")
    print("2 - Sair")

    acao = input("Informe o que deseja fazer: ")

    if acao == '0':
        nomeProduto = input("Informe o Nome do Produto: ").lower()
        if nomeProduto not in estoque:
            quantidade = int(input("Informe a quantidade do produto: "))
            estoque [nomeProduto] = quantidade
        else: print("Produto ja existe")
    
    elif acao == '1':
        consultarEstoque = input("Informe o nome do produto: ").lower()
        print(estoque.get(consultarEstoque, "Produto Nao Disponivel"))
    elif acao  == '2':
        print("Ate logo")
        break
    else: print("Digite uma acao Valida")
            

