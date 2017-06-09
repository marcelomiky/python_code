def menor_nome(nomes):
    
    tamanho = len(nomes) # pega a quantidade de nomes na lista
    menor = '' # variável para escolher o menor nome
    lista_limpa = [] # lista de nomes sem os espaços em branco
    
    # ignora espaços em branco
    for str in nomes:
        lista_limpa.append(str.strip())
        
    # verifica o menor nome
    menor = lista_limpa[0] # considera o primeiro como menor
    for str in lista_limpa:
        if len(str) < len(menor): # não deixei <= senão pegará um segundo menor de mesmo tamanho
            menor = str
            
    return menor.capitalize() # deixa a primeira letra maiúscula
