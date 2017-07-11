def inverte_sequencia():
    
    lista = []

    x = int(input("Digite um número (zero para sair):"))

    while x != 0:
        lista.append(x)
        x = int(input("Digite um número (zero para sair):"))

    lista = lista[::-1]
    
    def imprime(list):
        for i in list:
            print(i)
            
    return imprime(lista)
