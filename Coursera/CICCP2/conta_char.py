def conta_letras(frase, contar = 'vogais'):
    
    pos = len(frase) - 1 # atribui na variável pos (posição) a posição do array
    count = 0 # define o contador de vogais
    
    while pos >= 0: # conta as vogais
        if frase[pos] == 'a' or frase[pos] == 'e' or frase[pos] == 'i' or frase[pos] == 'o' or frase[pos] == 'u':
            count += 1
        pos = pos - 1
    
    if contar == 'consoantes':
        frase = frase.replace(' ', '')     # retira espaços em branco
        return len(frase) - count # subtrai do total as vogais
    else:
        return count
