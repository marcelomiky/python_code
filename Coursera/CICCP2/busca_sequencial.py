def busca(lista, elemento):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
