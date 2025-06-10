# Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.

def valorComDesconto(valorDaCompra):
    desconto = valorDaCompra * 0.10
    valorFinal = valorDaCompra - desconto
    return valorFinal

print(valorComDesconto(1000))