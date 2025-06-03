quantidadeDeEleitores = int(input("Informe o numero de Eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for count in range(quantidadeDeEleitores):
    print("Candidato 1: 1 \nCandidato 2: 2 \nCandidato 3: 3" )
    voto = int(input("Informe Numero do Candidato candidato: "))
    if voto == 1: candidato1 += 1
    elif voto == 2: candidato2 += 1
    elif voto == 3: candidato3 += 1
    else: print("Informe um candidato valido")

if candidato1 > candidato2 and candidato1 > candidato3: print(f"O Vencedor foi o Candidato 1 com {candidato1}")
elif candidato2 > candidato1 and candidato2 > candidato3: print(f"O Vencedor foi o Candidato 2 com {candidato2}")
elif candidato3 > candidato1 and candidato3 > candidato2: print(f"O Vencedor foi o Candidato 3 com {candidato3}")
else: print("Houve Empate"), print(f"Candidato 1: {candidato1}"), print(f"Candidato 2: {candidato2}"), print(f"Candidato 3: {candidato3}")