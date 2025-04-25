while True:
    nota = int(input("Informe uma nota(Entre 0 e 10): "))
    if nota >= 0 and nota <= 10:
        print(nota)
        break
    else: print("Informe uma nota valida")