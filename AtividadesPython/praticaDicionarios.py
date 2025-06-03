# Dicionarios sao uma especie de Atribuição


# Para criar um Dicionario  se coloca o 
# nomeDaFunção depois entre [] se coloca a chave e depois se coloca a tradução ou endereço 
# tradução não é um nome realmente justo, esta mais para valor de endereço ou valor do index
# a chave pode ser qualquer coisa, desde uma letra a um numero

tradutor = {}
tradutor1 = {"Pineapple": 'Abacaxi', "Apple": 'Maça', "Orange" : 'Laranja'} 
tradutor ["Pineapple"] = 'Abacaxi'
tradutor ["Apple"] = 'Maça'
tradutor ["Orange"] = 'Laranja'

# ao usar o print(type), ele aparecera como 'dict'
# print(type(tradutor))
# print(tradutor)
# se for letra usa-se ""/'' aspas, se for um nimero não precisa
# para printar se usa [chave] e a chave que foi definida
# print(tradutor['Apple'])

# o del deleta chave-valor
# para usar se passa a chave

# del (tradutor['Apple'])
# print(tradutor)

# pop se é igual o del
# a diferença que vc pode passar uma mensagem caso não seja encontrado o elemento

# tradutor.pop('Apple')

# print(tradutor.pop("banana", 'Fruta nao encontrada'))
# print(tradutor)

# o clear limpa todo o dicionario
# tradutor.clear()
# print(tradutor)

# o 'in' so verifica as chaves do dicionario
# para verificar/obter os valores se usa o 'values'
#print('laranja' in tradutor.values())
# print(tradutor.values())

# para alterar um valor se passa a chave existente e depois o novo valor
# Nao tem como mudar a chave, Para mudar a chave tem que criar outra0
# tradutor ['Apple'] = "IS Maça"
# print(tradutor)

# É possivel criar um dicionario dentro de outro

dados = {'Crossfox':{'km': 35000, 'ano': 2005}, 'Dss':{'Km': 17000,'Ano': 2015}, 
         'Fusca':{'Km': 130000,'Ano': 1979}, 'Jetta':{'Km': 56000,'Ano': 2011}, 'Passat':{'Km': 62000,'Ano': 1999}}

# print(dados)
# print(dados['Crossfox'])
# print(dados['Crossfox']["ano"])

# para localizar um elemento em um dicionario usa-se get
# print(dados.get('Gol', 'Veículo nao encontrado'))
# print(dados.get('Fusca', 'Veículo nao encontrado'))