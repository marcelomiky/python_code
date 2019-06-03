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


def intersection(lst1, lst2):  # From here: https://www.geeksforgeeks.org/python-intersection-two-lists/
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def multiply(numbers):  # From here: https://www.w3resource.com/python-exercises/python-functions-exercise-3.php
    total = 1
    for x in numbers:
        total *= x
    return total


def mdc(var1, var2):
    lista_primos_var1 = cria_lista_numeros_primos_ate_n_sobre_2(var1)

    divisor = lista_primos_var1[1]
    # print("Divisor[0]:", divisor)
    counter = 0
    lista_divisores1 = list()
    temp_var1 = var1
    
    while temp_var1 != 1:
        if temp_var1 % divisor == 0:
            lista_divisores1.append(divisor)
            temp_var1 /= divisor
        else:
            counter += 1
            divisor = lista_primos_var1[counter]

    lista_primos_var2 = cria_lista_numeros_primos_ate_n_sobre_2(var2)

    divisor = lista_primos_var2[1]
    # print("Divisor[0]:", divisor)
    counter = 0
    lista_divisores2 = list()
    temp_var2 = var2

    while temp_var2 != 1:
        if temp_var2 % divisor == 0:
            lista_divisores2.append(divisor)
            temp_var2 /= divisor
        else:
            counter += 1
            divisor = lista_primos_var2[counter]

    lista_interseccao_divisores = intersection(lista_divisores1, lista_divisores2)

    return multiply(lista_interseccao_divisores)


a = 12
b = 8

print("MDC({},{}) = {}".format(a, b, mdc(a, b)))


# mdc(24,8)

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
