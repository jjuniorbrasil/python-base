lista_palavras = ['Pá', 'Par', 'Parte', 'Partição', 'Particionado', 'Participações']

def maior_palavra(lista):
    maior_palavra = max(lista, key=len)
    return maior_palavra

print(maior_palavra(lista_palavras))