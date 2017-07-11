def remove_repetidos(lista):
    
    lista_aux = []
    
    for i in lista:
        if i not in lista_aux:
            lista_aux.append(i)
    
    lista_aux.sort()
    
    return lista_aux
