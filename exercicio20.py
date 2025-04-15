nota1 = float(input("Informe a Primeira Nota: "))
nota2 = float(input("Informe a Segunda Nota: "))
media = (nota1 + nota2) / 2

if media < 7: print(f"Reprovado \n Média: {media:.3f}")
elif media >= 7 and media < 10: print(f"Aprovado \n Média: {media:.3f}")
elif media == 10: print(f"Aprovado com Distinção \n Média: {media:.3f}")
else: print("Informe notas validas")