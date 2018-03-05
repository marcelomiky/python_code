def divide_grupos(alunos, grupos):
	'''
	Função que recebe a quantidade de alunos e grupos e faz a divisão dos grupos, agora sim de forma otimizada. 

    Se for uma divisão exata, retorna a quantidade de alunos por grupo. 

    Se não for uma divisão exata, a lista apresenta: [quantidade de grupos do tipo 1, quantidade de alunos por grupo do tipo 1, quantidade de grupos do tipo 2, quantidade de alunos por grupo do tipo 2] 
	
	>>> divide_grupos(40, 5)
	8
	
	>>> divide_grupos(20, 4)
	5

	>>> divide_grupos(21, 4)
	[3, 5, 1, 6]

	>>> divide_grupos(38, 8)
	[7, 5, 1, 3]
	'''
    
    if alunos % grupos == 0:
        return alunos // grupos
    elif (alunos % grupos < alunos // grupos):
        lista = []
        al1 = alunos // grupos
        gr1 = grupos - 1
        gr2 = grupos - gr1
        al2 = alunos - gr1 * al1
        lista.append(gr1)
        lista.append(al1)	
        lista.append(gr2)
        lista.append(al2)
        return lista
    else:
        lista = []
        al1 = alunos // grupos
        al1 += 1
        gr1 = grupos - 1
        gr2 = grupos - gr1
        al2 = alunos - gr1 * al1
        lista.append(gr1)
        lista.append(al1)	
        lista.append(gr2)
        lista.append(al2)
        return lista
            

	if __name__ == '__main__':
		import doctest
		doctest.testmod()	
