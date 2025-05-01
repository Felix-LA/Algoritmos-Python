nomeProduto = ['Caderno', 'Caneta', 'Lapis', 'Borracha', 'Regua']
codigoProduto = [10, 20, 30, 40, 50] 
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




    
    elif acao == "R":
        print(nomeProduto)
        print(codigoProduto)
        print(quantidadeProduto)

    elif acao == "S":
        print("Ate Mais")
        break