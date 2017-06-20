def ordena(lista):
    
    fim = len(lista)
    
    for i in range(fim - 1):
        min = i
        
        for j in range(i + 1, fim):
            if lista[j] < lista[min]:
                min = j
    
        lista[i], lista[min] = lista[min], lista[i]
    
    return lista
