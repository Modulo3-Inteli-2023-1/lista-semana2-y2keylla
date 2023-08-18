#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(str):
    palavra = str.split()
    palavras_unicas = set()

    for p in palavra:
        if p not in palavras_unicas:
            palavras_unicas.add(p)
    return len(palavras_unicas)
# Exemplo de uso:
frase = "Oi tudo bem bem"
print(conta_palavras_unicas(frase))



# Teste a sua função aqui (caso ache necessário)











