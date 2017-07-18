def inverte_sequencia():
    
    lista = []

    while True:
        x = int(input("Digite um número:"))
        if x != 0:
            lista.append(x)
        else:
            break        

    lista = lista[::-1]
    
    def imprime(list):
        for i in list:
            print(i)
            
    return imprime(lista)
