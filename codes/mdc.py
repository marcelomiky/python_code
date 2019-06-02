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
    print("Lista primos:", lista_primos)
    
    resto_lista_divisores_1 = 2 # número aleatório, diferente de 1, pra começar
    divisor = lista_primos[1]
    print("Divisor[0]:", divisor)
    counter = 0
    lista_divisores1 = [lista_primos[0]]
    temp_var1 = var1
    
    # while resto_lista_divisores_1 != 1:
    while counter <= len(lista_primos)-1:
        print("Counter(0):", counter)
        print("temp_var1:", temp_var1)
        print("Divisor dentro while", divisor)
        #if type(temp_var1 / divisor) == int:
        if temp_var1 % divisor == 0:
            print("!!Divisor:", divisor)
            lista_divisores1.append(divisor)
            resto_lista_divisores1 = temp_var1 / divisor
            print("resto lista divisores:", resto_lista_divisores_1)
            temp_var1 = resto_lista_divisores1
        else:
            print('caiu no ELSE')
            divisor = lista_primos[counter]
            counter += 1
            

    print("Lista divisores:", lista_divisores1)

mdc(12,8)
    
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
