# Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).
import random

def embaralhamento(frase):
    convertendoEmCaracteres = list(frase)
    random.shuffle(convertendoEmCaracteres)
    fraseEmbaralhada = ''.join(convertendoEmCaracteres)
    return print(fraseEmbaralhada)


embaralhamento("fraseTeste")