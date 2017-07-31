import re

def le_assinatura():
  
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a 
    ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_tamanho_medio(texto):
    
    '''Função que faz o primeiro cálculo: Tamanho médio de palavra é a soma dos tamanhos das 
    palavras dividida pelo número total de palavras.'''
    
    numero_palavras = 0
    soma_tamanhos_palavra = 0
    
    lista_palavras = separa_palavras(texto)
    
    for palavra in lista_palavras:
        numero_palavras += 1
        soma_tamanhos_palavra += len(palavra)
        
    return soma_tamanhos_palavra/numero_palavras

def calcula_type_token(texto):
    '''Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. 
    Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) 
    mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4/5 = 0.8'''
    
    numero_palavras = 0
    
    lista_palavras = separa_palavras(texto)
    
    numero_palavras_diferentes = n_palavras_diferentes(lista_palavras)    
    
    for palavra in lista_palavras:
        numero_palavras += 1    

    return numero_palavras_diferentes / numero_palavras

def calcula_hapax_legomana(texto):
    
    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido 
    pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total 
    (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). 
    Nessa frase, a relação Hapax Legomana vale 3/5 = 0.6'''
    
    numero_palavras = 0
    
    lista_palavras = separa_palavras(texto)
    
    numero_palavras_diferentes = n_palavras_unicas(lista_palavras)    
    
    for palavra in lista_palavras:
        numero_palavras += 1    

    return numero_palavras_diferentes / numero_palavras

def calcula_tamanho_medio_sentença(texto):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida 
    pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados 
    como parte da sentença).
    '''
    
    numero_sentenças = 0
    
    lista_sentenças = separa_sentencas(texto)
    
    frases = ''
    
    for sentença in lista_sentenças:
        frases += sentença
        numero_sentenças += 1
    
    lista_frases = separa_frases(frases)
    
    lista_palavras = ''
    
    for frase in lista_frases:
        lista_palavras += frase        
    
    palavras = separa_palavras(lista_palavras)
    
    caracteres_totais = 0
    
    for i in lista_palavras:
        caracteres_totais += len(i)
    
    return caracteres_totais / numero_sentenças

def calcula_complexidade_sentença(texto):
    
    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    
    número_frases = 0
    número_sentenças = 0
    
    lista_sentenças = separa_sentencas(texto)
    
    frases = ''
    
    for sentença in lista_sentenças:
        frases += sentença
    
    lista_frases = separa_frases(frases)
    
    número_frases = len(lista_frases)
    número_sentenças = len(lista_sentenças)
    
    return número_frases / número_sentenças

def calcula_tamanho_medio_frase(texto):
    
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo 
    número de frases no texto (os caracteres que separam uma frase da outra não devem ser 
    contabilizados como parte da frase).'''
    
    lista_sentenças = separa_sentencas(texto)
    
    frases = ''
    
    for sentença in lista_sentenças:
        frases += sentença
    
    lista_frases = separa_frases(frases)
    
    número_frases = len(lista_frases)
    
    lista_palavras = ''
    
    for frase in lista_frases:
        lista_palavras += frase        
    
    palavras = separa_palavras(lista_palavras)
    
    caracteres_totais = 0
    
    for i in lista_palavras:
        caracteres_totais += len(i)
        
    return caracteres_totais / número_frases

def calcula_assinatura(texto):
    
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    if type(texto) != list:
        aux = texto
        texto = []
        texto.append(aux)
    
    matriz_ass_input = []
    
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))  # sent.. = lista comum, ~matriz
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)  # frases = matriz, lista de listas
            num_tot_sentencas += 1
            soma_cat_sentencas = soma_cat_sentencas + len(sentencas[i])
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                palavra_i = separa_palavras(str(frases[lin][col]))
                palavras.append(palavra_i)  # palav.. = matriz, lista de listas
                num_tot_frases += 1
                soma_cat_frases = soma_cat_frases + len(str(frases[lin][col]))
        mtrx_para_lista = []  # transform.. palavras de matriz para lista
        
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                mtrx_para_lista.append(palavras[lin][col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras = soma_comp_palavras + len(str(palavras[lin][col]))
            num_tot_palavras += 1
        ass_txt = []
        ass_txt.append(calcula_tamanho_medio(soma_comp_palavras, num_tot_palavras))
        ass_txt.append(calcula_type_token(palavras, num_tot_palavras))
        ass_txt.append(calcula_hapax_legomana(palavras, num_tot_palavras))
        ass_txt.append(calcula_tamanho_medio_sentença(soma_cat_sentencas, num_tot_sentencas))
        ass_txt.append(calcula_complexidade_sentença(num_tot_frases, num_tot_sentencas))
        ass_txt.append(calcula_tamanho_medio_frase(soma_cat_frases, num_tot_frases))
        matriz_ass_input.append(ass_txt)
    
    return matriz_ass_input  # matriz, lista de listas dos valores das assina..

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de 
    similaridade nas assinaturas.'''
    
    #grau_similaridade = 0
    
    #for i in range(7):
    #    grau_similaridade += (as_a[i] - as_b[i])
    
    #grau_similaridade /= 6    
    
    #return grau_similaridade
    
    lista_Sab = []
    soma_mod = 0
    if type(matriz_ass_input[0]) is list:
        for lin in range(len(matriz_ass_input)):
            for col in range(len(matriz_ass_input[lin])):
                soma_mod += abs(ass_main[col] - matriz_ass_input[lin][col])
            Sab = soma_mod / 6
        lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(matriz_ass_input)):
            soma_mod += abs(ass_main[i] - matriz_ass_input[i])
        Sab = soma_mod / 6
    return Sab

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto 
    com maior probabilidade de ter sido infectado por COH-PIAH.'''

    aux_ass_com = ass_comparadas[:]
    aux_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if aux_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah

def main():
    ass_main = le_assinatura()
    textos_main = le_textos()
    matriz_ass = calcula_assinatura(textos_main)
    ass_comparadas = compara_assinatura(ass_main, matriz_ass)
    copiah = avalia_textos(textos_main, ass_comparadas) + 1
    return print("O autor do texto", copiah, "está infectado com COH-PIAH.")

if __name__ == "__main__":
    main()




























