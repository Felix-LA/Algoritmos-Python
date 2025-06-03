while True:
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    candidato4 = 0
    votosNulos = 0
    votosEmBranco = 0

    voto = int(input("Informe o candidato que deseja votar: "))
    
    if voto == 0: 
        print()
        print()
        print("Votos")
        print()

        print(f"Canditato 1: {candidato1}")
        print(f"Canditato 2: {candidato2}")
        print(f"Canditato 3: {candidato3}")
        print(f"Canditato 4: {candidato4}")
        print(f"Votos Nulos foi: {votosNulos}")
        print(f"Votos em Branco foi: {votosEmBranco}")
        break

    elif voto == 1: 
        candidato1 += 1 
        print("Voto Computado")

    elif voto == 2: 
        candidato2 += 1 
        print("Voto Computado")
    
    elif voto == 3: 
        candidato3 += 1
        print("Voto Computado")
    
    elif voto == 4:
        candidato4 += 1
        print("Voto Computado")
    
    elif voto == 5: 
        votosNulos += 1 
        print("Voto Computado")
    
    elif voto == 6: 
        votosEmBranco += 1 
        print("Voto Computado")
    
    else: print("Faça uma ação valida")

