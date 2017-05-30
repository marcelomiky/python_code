def dimensoes(A):
    
    '''Função que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
    
    Obs: i = colunas, j = linhas
    
    Exemplo: 
    >>> minha_matriz = [[1], 
                        [2], 
                        [3]
                        ]
    >>> dimensoes(minha_matriz)
    >>> 3X1
    '''
    
    lin = len(A)
    col = len(A[0])
    
    return print("%dX%d" % (lin, col))
