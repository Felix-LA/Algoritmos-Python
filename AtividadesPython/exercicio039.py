traducaoDePalavras = {
    "apple": "maçã", "banana": "banana",
    "cat": "gato", "dog": "cachorro",
    "elephant": "elefante", "fish": "peixe",
    "grape": "uva", "house": "casa",
    "island": "ilha", "jungle": "selva",
    "king": "rei", "lion": "leão",
    "mountain": "montanha", "night": "noite",
    "orange": "laranja", "pencil": "lápis",
    "queen": "rainha", "rose": "rosa",
    "sun": "sol", "tree": "árvore",
    "umbrella": "guarda-chuva", "village": "vila",
    "water": "água", "xylophone": "xilofone",
    "yellow": "amarelo", "zebra": "zebra",
    "airplane": "avião", "ball": "bola",
    "car": "carro", "door": "porta",
    "ear": "orelha", "flower": "flor",
    "guitar": "guitarra", "hat": "chapéu",
    "ice": "gelo", "juice": "suco",
    "key": "chave", "lamp": "lâmpada",
    "moon": "lua", "nose": "nariz",
    "ocean": "oceano", "pen": "caneta",
    "queen": "rainha", "rain": "chuva",
    "star": "estrela", "table": "mesa",
    "umbrella": "guarda-chuva", "vase": "vaso",
    "window": "janela", "x-ray": "raio-x",
    "yarn": "fio", "zoo": "zoológico",
    "air": "ar", "balloon": "balão",
    "cloud": "nuvem", "doghouse": "casinha de cachorro",
    "elephant": "elefante", "fire": "fogo",
    "grape": "uva", "hat": "chapéu",
    "icecream": "sorvete", "jacket": "jaqueta",
    "kite": "pipa", "lemon": "limão",
    "mountain": "montanha", "night": "noite",
    "orange": "laranja", "pizza": "pizza",
    "queen": "rainha", "rose": "rosa",
    "sun": "sol", "tree": "árvore",
    "umbrella": "guarda-chuva", "vase": "vaso",
    "water": "água", "xylophone": "xilofone",
    "yellow": "amarelo", "zebra": "zebra",
    "airplane": "avião", "ball": "bola",
    "car": "carro", "door": "porta",
    "ear": "orelha", "flower": "flor",
    "guitar": "guitarra", "hat": "chapéu",
    "ice": "gelo", "juice": "suco",
    "key": "chave", "lamp": "lâmpada",
    "moon": "lua", "nose": "nariz",
    "ocean": "oceano", "pen": "caneta",
    "queen": "rainha", "rain": "chuva",
    "star": "estrela", "table": "mesa",
    "umbrella": "guarda-chuva", "vase": "vaso",
    "window": "janela", "x-ray": "raio-x",
    "yarn": "fio", "zoo": "zoológico",
    "air": "ar", "balloon": "balão",
    "cloud": "nuvem", "doghouse": "casinha de cachorro",
    "elephant": "elefante", "fire": "fogo",
    "grape": "uva", "hat": "chapéu",
    "icecream": "sorvete", "jacket": "jaqueta",
    "kite": "pipa", "lemon": "limão",
    "mountain": "montanha", "night": "noite",
    "orange": "laranja", "pizza": "pizza",
    "queen": "rainha", "rose": "rosa",
    "sun": "sol",     "tree": "árvore",
    "umbrella": "guarda-chuva", "vase": "vaso",
    "water": "água", "xylophone": "xilofone",
    "yellow": "amarelo", "zebra": "zebra",
    "airplane": "avião", "ball": "bola",
    "car": "carro", "door": "porta",
    "ear": "orelha", "flower": "flor",
    "guitar": "guitarra", "hat": "chapéu",
    "ice": "gelo", "juice": "suco",
    "key": "chave", "lamp": "lâmpada",
    "moon": "lua", "nose": "nariz",
    "ocean": "oceano", "pen": "caneta",
    "queen": "rainha", "rain": "chuva",
    "star": "estrela", "table": "mesa",
    "umbrella": "guarda-chuva", "vase": "vaso",
    "window": "janela", "x-ray": "raio-x",
    "yarn": "fio", "zoo": "zoológico"}


while True:
    print("-----MENU-----")
    print("0 - Adicionar uma Palavra")
    print("1 - Consultar Palavra")
    print("2 - Sair")
    acao = input("Informe o que deseja fazer: ")

    if acao == '0':
        palavra = input("Informe uma palvra(Em Ingles): ").lower()
        palavraTraducao = input("Informe a Tradução(Em portugues): ").lower()
        if palavra not in traducaoDePalavras:
            traducaoDePalavras [palavra] = palavraTraducao
        else: print("Palavra ja existe!!!")

    elif acao == '1':
        palavra = input("Informe uma palvra(Em Ingles): ").lower()
        print(traducaoDePalavras.get(palavra, "Palavra Nao encontrada"))
    elif acao == '2':
        print("Ate Mais !!!")
        break
    else: print("Faça uma açao valida")
