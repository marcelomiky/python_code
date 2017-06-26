def busca(lista, elemento):
    
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            print(meio)
            return meio
        else:
            if elemento < lista[meio]: # busca na primeira metade da lista
                ultimo = meio - 1 # já foi visto que não está no elemento meio, então vai um a menos
                print(meio) # função deve imprimir cada um dos índices testados pelo algoritmo.
            else: 
                primeiro = meio + 1
                print(meio)
    return False
