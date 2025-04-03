lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)
print()
print(lista[1:10])
print()
print(lista[8:])
print()

# forma de pegar so numeros pares em uma lista
# for i in range(len(lista)):
#     if i % 2 == 0:
#         print(lista[i])
print(lista[0::2])

print()
# forma de pegar so numeros IMpares em uma lista
# for i in range(len(lista)):
#     if i % 2 != 0:
#         print(lista[i])
# forma de pular caracteres em uma lista
print(lista[1::2]) 

# print(list[comeco:fim:pulo])
print()
# reverter lista

print(lista[:: -1])
lista.sort(reverse=True)
print(lista)
