# Crie uma função que receba uma string e retorne a mesma string sem espaços.

def removerEspacosDoTexto(texto):
    textoSemEspacos = ""

    for caractere in texto:
        if caractere != " ":
            textoSemEspacos += caractere

    return textoSemEspacos

frase = "Transformando frase com espaco em frase sem espaco"
print(removerEspacosDoTexto(frase))