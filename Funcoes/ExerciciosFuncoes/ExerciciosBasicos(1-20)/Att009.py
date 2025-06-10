# # Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.

def nomesMaioresQue5(nomes):
    nomesFiltrados = []

    for nome in nomes:
        if len(nome) > 5:
            nomesFiltrados.append(nome)

    return nomesFiltrados

lista = ["Ana", "Roberto", "Lucas", "Fernanda", "João"]
print(nomesMaioresQue5(lista))