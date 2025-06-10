# Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.

def contarElementos(lista):
    contagem = {}
    
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1 
        else:
            contagem[elemento] = 1  
    
    return contagem


teste = ['a', 'b', 'a', 'c', 'b', 'a']
print(contarElementos(teste))
