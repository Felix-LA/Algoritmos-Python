numero = int(input("Informe o numero da sequencia: "))
sequencia = []
numeroAnterior = 0
ultimoNumero = 1

for count in range(numero):
    sequencia.append(ultimoNumero)
    armazenamento = ultimoNumero
    ultimoNumero += numeroAnterior
    numeroAnterior = armazenamento
    
print(sequencia)