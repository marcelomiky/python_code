def sao_multiplicaveis(m1, m2):
    
    '''Recebe duas matrizes como parâmetros e devolve True se as matrizes forem   	 multiplicáveis (número de colunas 
       da primeira é igual ao número de linhs da segunda). False se não forem
    '''
    
    if len(m1) == len(m2[0]):
        return True
    else:
        return False
