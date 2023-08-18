#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
    lista1 = list(string1.lower())
    lista2 = list(string2.lower())

    lista1.sort()
    lista2.sort()

    return lista1 == lista2

# Exemplo de uso:
string1 = "Roma"
string2 = "amor"

if is_anagram(string1, string2):
    print(True)
else:
    print(False)






# Teste a sua função aqui (caso ache necessário)











