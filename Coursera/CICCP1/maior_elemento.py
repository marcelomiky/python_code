def maior_elemento(lista):
    
    maior = lista[0]
    
    for i in lista:
        if maior < i:
            maior = i
    
    return maior
