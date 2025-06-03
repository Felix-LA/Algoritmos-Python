
#cria um arquivo se nao existir
#Forma de abrir arquivos
# passe uma variavel para salvar o arquivo
# a = open("file.txt", "r")


#Forma de ler o arquivo
# print(a.read())


#Fechar arquivo
# a.close()

#Forma de adicionar conteudo
# a de apend, para adicionar conteudo
# b = open("file.txt", "a")
# b.write("Adicionando Conteudo")
# b = open("file.txt", "r")
# print(b.read())
# b.close()

# # pode passar uma variavel na hora de adicionar
# # use o utf-8 par a formatação, e para permitir que passe acentos,etc...
# c = open("file.txt", "a", encoding = "utf-8")
# x = input("Informe o seu Nome: ")
# c.write(x)
# #para pular linha passe um 
# c.write("\n")
# c = open("file.txt", "r")
# print(c.read())
# c.close()

# #forma de subescrever um programa
# #cria um arquivo se nao existir
# #se ja existir conteudo ele ira sobre-escrever o conteudo
# d = open("file.txt", "w")
# d.write("aaaaa")
# d = open("file.txt", "r")
# print(d.read())
# d.close()


#so cria o arquivo
# da erro se o arquivo ja existir
# e = open("file.txt", "x")

# #pode-se especificar como eu quero que ele seja lido
# #para texto
# b = open("file.txt", "rt")
# #para binario
# # bastante usado para imagens
# b = open("file.txt", "rb")

# pode-se usar o With open em banco de daos tambem
# mais seguro
# forma de abrir e fechar o arquivo txt
# ele abre, faz o que vc quiser e depois fecha sem precisar do .close()
# with open ("file.txt", "a") as x:
#     x.write("Novo cadastro\n")


# mostra a linha, ler a linha
# with open ("file.txt", "r") as x:
#     linhas = x.readlines()
#     print(linhas[2])


# forma de deletar as linhas
# with open ("file.txt", "r") as x:
#     linhas = x.readlines()
#     del linhas[2]
# with open("file.txt", "r") as x:
#     x.writelines(linhas)
     

