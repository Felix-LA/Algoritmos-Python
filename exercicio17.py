nomeProduto1 = input("Informe o Nome do Produto: ")
valorProduto1 = float(input("Informe o Preço do Produto: "))

nomeProduto2 = input("Informe o Nome do Produto: ")
valorProduto2 = float(input("Informe o Preço do Produto: "))

nomeProduto3 = input("Informe o Nome do Produto: ")
valorProduto3 = float(input("Informe o Preço do Produto: "))

if valorProduto1 < valorProduto2 and valorProduto1 < valorProduto3: print("O produto a ser comprado é o produto {0} com o valor de {1:.2f}" .format(nomeProduto1 , valorProduto1))
elif valorProduto2 < valorProduto1 and valorProduto2 < valorProduto3: print("O produto a ser comprado é o produto {0} com o valor de {1:.2f}" .format(nomeProduto2 , valorProduto2))
elif valorProduto3 < valorProduto1 and valorProduto3 < valorProduto2: print("O produto a ser comprado é o produto {0} com o valor de {1:.2f}" .format(nomeProduto3 , valorProduto3))
else: print("Produtos com valores IGUAIS ANIMAL")
