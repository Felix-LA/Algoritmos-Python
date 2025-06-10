# Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.

def calcularJurosCompostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    return montante

print(calcularJurosCompostos(1000.00, 0.05, 3))