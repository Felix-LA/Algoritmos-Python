# Escreva uma função que receba uma frase e retorne a quantidade de palavras.

def contadorDePalavras(frase):
    palavras = frase.split()
    return print(f"A quantidade de palavras na frase: {frase} é: {len(palavras)}")
    

teste = "A quantidade de Palavras é 6"
contadorDePalavras(teste)
