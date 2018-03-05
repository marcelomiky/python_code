def divide_grupos(alunos, grupos):
    """Function that gets the total of students and groups and does the division, in a optimized way.
    If it's a round division, returns the number of students per group
    If it's not a round division, the list presents:
    [quantity of groups of type 1 quantity of students per groups of type 1, quantity of groups of type 1 quantity of students per groups of type 2]

    >>> divide_grupos(40, 5)
    8

    >>> divide_grupos(20, 4)
    5

    >>> divide_grupos(21, 4)
    [3, 5, 1, 6]

    >>> divide_grupos(38, 8)
    [6, 5, 2, 4]
    """
    
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
        if al1 - al2 >= 2:
            lista_nova = []
            gr1 -= 1
            gr2 += 1
            al2 += 1
            lista_nova.append(gr1)
            lista_nova.append(al1)	
            lista_nova.append(gr2)
            lista_nova.append(al2)
            return lista_nova
        else:
            lista.append(gr1)
            lista.append(al1)	
            lista.append(gr2)
            lista.append(al2)
            return lista
            

    if __name__ == '__main__':
        import doctest
        doctest.testmod()
