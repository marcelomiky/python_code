def eh_primo(x):
    """
    Função que determina se o número x é primo ou não
    
    return 1: é primo
    return 0: não é primo
    """
    num_divisores = 0
    
    for i in range(1, x+1):
        if x % i == 0:
            num_divisores += 1
    
    if num_divisores > 2:
        return 0
    else:
        return 1

#print(eh_primo(3))
#print(eh_primo(2))
#print(eh_primo(17))


def cria_lista_numeros_primos_ate_n_sobre_2(n):
    """
    Função que retorna todos os números primos de 1 até n/2
    """
    lista_primos = list()
    for i in range(1, n//2):
        if eh_primo(i) == 1:
            lista_primos.append(i)

    return lista_primos

#print(cria_lista_numeros_primos_ate_n_sobre_2(30))  # [1, 2, 3, 5, 7, 11, 13]
#print(cria_lista_numeros_primos_ate_n_sobre_2(20))  # [1, 2, 3, 5, 7]


def mdc(var1, var2):
    lista_divisores_1 = list()
    lista_divisores_2 = list()
    
    if var1 > var2:
        lista_primos = cria_lista_numeros_primos_ate_n_sobre_2(var1)
    else:
        lista_primos = cria_lista_numeros_primos_ate_n_sobre_2(var2)
    
    #lista_primos = [2, 3, 5, 7, 11]
    
#    resto_lista_divisores_1 = 2 # número aleatório, diferente de 1, pra começar
    divisor = lista_primos[0]
   
    while var1 % divisor != 1:
        var1_temp = va1 / divisor
            lista_divisores1.append(lista_primos[0])
                
    
    # Pega a intersecção deles
    # intersec =
    
    # Multiplica todos os valores da intersecção entre eles
            
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
