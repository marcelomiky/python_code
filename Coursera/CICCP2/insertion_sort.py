def insertion_sort(lista):

    fim = len(lista)

    for i in range(fim - 1):
        posicao_do_minimo = i

        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]: 
                posicao_do_minimo = j            
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    
    return lista
