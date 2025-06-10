# Crie uma função que substitua todas as vogais de uma string por "*".

def substituirVogais(texto):
    vogais = "aeiouAEIOU"
    resultado = ""
    for caracteres in texto:
        if caracteres in vogais:
            resultado += "*"
        else:
            resultado += caracteres
    return print(resultado)

teste = "Python é divertido"
substituirVogais(teste)