def mdc(var1, var2):
    lista_divisores_1 = list()
    lista_divisores_2 = list()
    
    lista_primos = [2, 3, 5, 7, 11]
    
    resto_lista_divisores_1 = 2 # número aleatório, diferente de 1, pra começar
    while resto_lista_divisores_1 != 1:
        if var1 % lista_primos[0] == 0:
            lista_divisores1.append(lista_primos[0])
            
"""
Ex:

mdc(12,8)

12 | 2
6  | 2
3  | 3
1

8 | 2
4 | 2
2 | 2
1

portanto, mdc(12,8) = 2*2 = 4

"""
