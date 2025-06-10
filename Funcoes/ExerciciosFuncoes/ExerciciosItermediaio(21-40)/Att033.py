# Escreva uma função que recebe um número decimal e retorna sua representação binária.
import os


def representacaoBinaria(numeroDecimal):
    valorBinario = ''
    while numeroDecimal > 0:
        novovalor = numeroDecimal % 2
        novovalor = int(novovalor)
        numeroDecimal /= 2
        numeroDecimal = int(numeroDecimal)
        valorBinario = str(novovalor) + valorBinario

    return valorBinario

print(representacaoBinaria(5))