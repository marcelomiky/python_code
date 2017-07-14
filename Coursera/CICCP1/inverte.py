def inverte_sequencia():
    
    lista = []

    while True:
        x = int(input("Digite um número (zero para sair):"))
        if x != 0:
            lista.append(x)
        else:
            break        
    
    for i in lista[::-1]:
        print(i)
