nomeProduto = ['Caderno', 'Caneta', 'Lapis', 'Borracha', 'Regua']
codigoProduto = [0, 1, 2, 3, 4] 
quantidadeProduto = [10, 10, 10, 10, 10,]

while True:
    
    print("-----MENU-----")
    print("E - Entrada no Estoque")
    print("S - Saida no Estoque")
    print("R - Relatorio")
    print("C - Cadastro de Produto")
    print("S - Sair")
    acao = input("Informe o que deseja fazer: ").upper()

    
    if acao == "E":
        print(nomeProduto)
        print(codigoProduto)
        print(quantidadeProduto)
        acaoEstoque = int(input("Informe o Codigo do Produto: "))
        if acaoEstoque in codigoProduto:
            acrescimo = int(input("Informe a Quantidade a ser acrescentada: "))
            quantidadeProduto[acaoEstoque] =+ quantidadeProduto[acaoEstoque] + acrescimo
        else: print("Produto nao encontrado")
    
    elif acao == "S":
        print(nomeProduto)
        print(codigoProduto)
        print(quantidadeProduto)
        acaoEstoque = int(input("Informe o Codigo do Produto: "))
        if acaoEstoque in codigoProduto:
            retirada = int(input("Informe a Quantidade a ser retirada: "))
            if retirada < quantidadeProduto[acaoEstoque]:
                quantidadeProduto[acaoEstoque] =+ quantidadeProduto[acaoEstoque] - retirada
            else: print("A quantidade a ser retirada é menor que no estoque")
    
    elif acao == "R":
        print(nomeProduto)
        print(codigoProduto)
        print(quantidadeProduto)

    elif acao == "C":
        novoProduto = input("Informe o nome do produto: ")
        quantidadeNovoProduto = int(input("Informe a Quantidade do Novo Produto: "))
        nomeProduto.append(novoProduto)
        quantidadeProduto.append(quantidadeNovoProduto)
        codigoNovoProduto = max(codigoProduto) + 1
        codigoProduto.append(codigoNovoProduto)

    elif acao == "S":
        print("Ate Mais")
        break