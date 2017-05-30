def soma_matrizes(m1, m2):
    
    def dimensoes(A):
        lin = len(A)
        col = len(A[0])
    
        return ((lin, col))
    
    if dimensoes(m1) != dimensoes(m2):
        return False
    else:
        matriz = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            matriz.append(linha)
        return matriz
