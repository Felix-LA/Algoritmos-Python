candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votosNulos = 0
votosEmBranco = 0
quantidadeDeVotos = 0
while True:

    voto = input("Informe o candidato que deseja votar: ")
    
    if voto == '0': 
        
        if candidato1 > candidato2 and candidato1 > candidato3 and candidato1 > candidato4:
            print()
            print("O Candidato 1 Ganhou: {0}".format(candidato1))

            print()
            print()
            print("Votos")
            print()

            print(f"Total de Votos: {quantidadeDeVotos}")
            print(f"Canditato 1: {candidato1}")
            print(f"Canditato 2: {candidato2}")
            print(f"Canditato 3: {candidato3}")
            print(f"Canditato 4: {candidato4}")
            print(f"Votos Nulos foi: {votosNulos}")
            print(f"Votos em Branco foi: {votosEmBranco}")

            break

        elif candidato2 > candidato1 and candidato2 > candidato3 and candidato2 > candidato4:
            print()
            print("O Candidato 2 Ganhou: {0}".format(candidato2))
            print()
            print()
            print("Votos")
            print()

            print(f"Total de Votos: {quantidadeDeVotos}")
            print(f"Canditato 1: {candidato1}")
            print(f"Canditato 2: {candidato2}")
            print(f"Canditato 3: {candidato3}")
            print(f"Canditato 4: {candidato4}")
            print(f"Votos Nulos foi: {votosNulos}")
            print(f"Votos em Branco foi: {votosEmBranco}")

            break

        elif candidato3 > candidato1 and candidato3 > candidato2 and candidato3 > candidato4:
            print()
            print("O Candidato 3 Ganhou: {0}".format(candidato3))
            print()
            print()
            print("Votos")
            print()

            print(f"Total de Votos: {quantidadeDeVotos}")
            print(f"Canditato 1: {candidato1}")
            print(f"Canditato 2: {candidato2}")
            print(f"Canditato 3: {candidato3}")
            print(f"Canditato 4: {candidato4}")
            print(f"Votos Nulos foi: {votosNulos}")
            print(f"Votos em Branco foi: {votosEmBranco}")

            break

        elif candidato4 > candidato1 and candidato4 > candidato3 and candidato4 > candidato3:
            print()
            print("O Candidato 4 Ganhou: {0}".format(candidato4))
            print()
            print()
            print("Votos")
            print()

            print(f"Total de Votos: {quantidadeDeVotos}")
            print(f"Canditato 1: {candidato1}")
            print(f"Canditato 2: {candidato2}")
            print(f"Canditato 3: {candidato3}")
            print(f"Canditato 4: {candidato4}")
            print(f"Votos Nulos foi: {votosNulos}")
            print(f"Votos em Branco foi: {votosEmBranco}")

            break
        else: 
            print()
            print("EMPATE")
            print()
            print()
            print("Votos")
            print()

            print(f"Total de Votos: {quantidadeDeVotos}")
            print(f"Canditato 1: {candidato1}")
            print(f"Canditato 2: {candidato2}")
            print(f"Canditato 3: {candidato3}")
            print(f"Canditato 4: {candidato4}")
            print(f"Votos Nulos foi: {votosNulos}")
            print(f"Votos em Branco foi: {votosEmBranco}")

            break
    

    elif voto == '1': 
        candidato1 =+ 1 
        quantidadeDeVotos += 1
        print("Voto Computado")

    elif voto == '2': 
        candidato2 += 1 
        quantidadeDeVotos += 1
        print("Voto Computado")
    
    elif voto == '3': 
        candidato3 += 1
        quantidadeDeVotos += 1
        print("Voto Computado")
    
    elif voto == '4':
        candidato4 += 1
        quantidadeDeVotos += 1
        print("Voto Computado")
    
    elif voto > '4': 
        votosNulos += 1 
        quantidadeDeVotos += 1
        print("Voto Computado")
    
    elif voto == '': 
        votosEmBranco += 1 
        quantidadeDeVotos += 1
        print("Voto Computado")
    
    else: print("Faça uma ação valida")

