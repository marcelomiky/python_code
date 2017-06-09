def maiusculas(frase):
    
    listRe = [] # lista de retorno vazia
    stringRe = '' # string de retorno vazia
    
    for ch in frase:
        if ord(ch) >=65 and ord(ch) <= 91:
            listRe.append(ch)      
    
    # retornando a lista para string
    stringRe = ''.join(listRe)
    
    return stringRe
