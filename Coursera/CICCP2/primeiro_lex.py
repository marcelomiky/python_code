def primeiro_lex(lista):
    
    resposta = lista[0] # define o primeiro item da lista como a resposta...mas verifica depois.
    
    for str in lista:
        if ord(str[0]) < ord(resposta[0]):
            resposta = str
    
    return resposta
