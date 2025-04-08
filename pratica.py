print("-- Reservatório de Água --") #Reservatorio esta escrito errado, faltou fechar o parenteses

altura = float(input(" Digite a altura (cm):"))
largura = int(input(" Digite a largura (cm): ")) # faltou fechar o parenteses
comprimento = float(input(" Digite o comprimento (cm): "))
c_diario = float(input("Digite o valor do consumo médio diário(litros/dia)= ")) # faltou '=' depois do c_diário e antes do float, acento em diario

cap_total = ((altura * largura * comprimento)/1000); '''o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros''' # Colocou virgula dentro do calculo
auton_reser = cap_total / c_diario

print("Capacidade do Reservatório = ",cap_total, "litros ") 
print("Autonomia do reservatório = ",auton_reser," dias"); '''Agora, vamos classificar o consumo''' # faltou a virgula para o comentario
if(auton_reser < 2):
     print("Consumo Elevado") #faltava identação
elif(auton_reser >= 2 and auton_reser == 7): # faltou o símbolo '=='
     print("Consumo Moderado")
elif(auton_reser > 7): #estava elif invez de if
	print("\n Consumo Baixo") #Identação