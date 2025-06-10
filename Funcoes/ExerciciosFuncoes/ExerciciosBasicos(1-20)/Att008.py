# Crie uma função que inverta uma string.

def reverterString(string):
    reverseString = "".join(reversed(string))
    print(reverseString)

reverterString("abc")