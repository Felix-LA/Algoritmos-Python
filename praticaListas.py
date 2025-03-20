frutas = ["maca", "laranja", "banana", "cereja"]

##Sinal de + usado para concatenar strings

print([1, 2] + [3, 4]) 
print(frutas + [6, 7, 8, 9])

##Sinal de * usado para fazer uma string se repetir quantas vezes requisitado
print(["teste"] * 4)
print([1, 2, ["Olá", "Adeus"]] * 2)
print()

print()
##Coloque sempre dentro de [], principalmente quando se usa numeros, para nao se usar a função matematica correspondente
print()


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

## min() pega o menor valor de uma lista
print(min(a))

## max() pega o maior valor de uma lista
print(max(a))

## sum() soma os valores de uma lista
print(sum(a))

print()
## so use numeros para 
print()


##função slice picota uma lista, seleciona os elementos selecionados
##ele pega o que vc selecionou ate o penultimo, se passar[0:3], vai selecionar do 0 ate o 2, o 3 é so para falar que vai ate aquele

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']

print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

print()
print()

##como modificar/alterar listas

frutas = ["banana", "maça", "cereja"]

print(frutas)
frutas[0] = "pera"
print(frutas)
frutas[-1] = "laranja"
print(frutas)

print()

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']

uma_lista[1:3] = 'x', 'y'

print(uma_lista)

print()

print(uma_lista)
print(len(uma_lista))

uma_lista[1:3] = []

print(uma_lista)
print(len(uma_lista))

print()
print()
print()

##uma forma de adicionar membros em uma lista

uma_lista = ['a', 'd', 'f']
print(uma_lista)
print(len(uma_lista))

uma_lista[1:1] = ['b', 'c']
print(uma_lista)
print(len(uma_lista))

uma_lista[4:4] = ['e']
print(uma_lista)
print(len(uma_lista))

##sempre usar posições exatas/iguais
##ele passa uma lista no lugar e manda o que tinha no lugar para frente
##não é uma forma adequada de adicinar elementos em uma lista, basicamente espremendo elementos dentro da lista
##nao confundir com o metodo de substituir

print()
print()
print()

##Comando del para deletar itens

a = ['um','dois', 'tres']

del a[1]
print(a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)