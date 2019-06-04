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


def cria_lista_numeros_primos_ate_n(n):
    """
    Função que retorna todos os números primos de 1 até n
    """
    lista_primos = list()
    for i in range(1, n):
        if eh_primo(i) == 1:
            lista_primos.append(i)

    return lista_primos


# print(cria_lista_numeros_primos_ate_n(30))  # [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print(cria_lista_numeros_primos_ate_n(20))  # [1, 2, 3, 5, 7, 11, 13, 17, 19]


def lista_divisores_do_mdc(x):
    lista_primos = cria_lista_numeros_primos_ate_n(x)
    divisor = lista_primos[1]
    counter = 0
    lista_divisores = [lista_primos[0]]
    temp_x = x

    while temp_x != 1:
        if temp_x % divisor == 0:
            lista_divisores.append(divisor)
            temp_x /= divisor
        else:
            counter += 1
            divisor = lista_primos[counter]

    return lista_divisores


# x = 1024
# print(lista_divisores_do_mdc(x))


def lista_divisores(x):

    lista_para_dividir = list(range(1, (x)//2 + 1))
    lista_divisores = list()
    temp_x = x

    for i in lista_para_dividir:
        if temp_x % i == 0:
            lista_divisores.append(i)

    lista_divisores.append(x)

    return lista_divisores


# x = 100
# print("lista_divisores(x)", lista_divisores(x))


def intersection(lst1, lst2):  # From here: https://www.geeksforgeeks.org/python-intersection-two-lists/
    lst3_temp1 = [value for value in lst1 if value in lst2]
    lst3_temp2 = [value for value in lst2 if value in lst1]

    # print("TEMP1: {}. TEMP2: {}".format(lst3_temp1, lst3_temp2))
    if len(lst3_temp1) < len(lst3_temp2):
        return lst3_temp1
    else:
        return lst3_temp2


def numeros_primos_entre_si(a, b):
    if eh_primo(a) == 1 and eh_primo(b) == 1:
        return 1
    elif len(intersection(lista_divisores(a), lista_divisores(b))) == 1:
        return 1
    else:
        return 0


# print(cria_lista_numeros_primos_ate_n(3))
# print(cria_lista_numeros_primos_ate_n(4))
# print("numeros_primos_entre_si(3, 4):", numeros_primos_entre_si(3, 4))


def multiply(numbers):  # From here: https://www.w3resource.com/python-exercises/python-functions-exercise-3.php
    total = 1
    for x in numbers:
        total *= x
    return total


def mdc(var1, var2):

    if numeros_primos_entre_si(var1, var2):  # para quando faz mdc entre números primos entre eles, como 3 e 4
        return 1
    else:
        lista_divisores1 = lista_divisores_do_mdc(var1)
        lista_divisores2 = lista_divisores_do_mdc(var2)

        # lista_primos_var1 = cria_lista_numeros_primos_ate_n(var1)
        #
        # print("lista_primos_var1:", lista_primos_var1)
        #
        # divisor = lista_primos_var1[1]
        # # print("Divisor[0]:", divisor)
        # counter = 0
        # lista_divisores1 = list()
        # temp_var1 = var1
        #
        # while temp_var1 != 1:
        #     if temp_var1 % divisor == 0:
        #         lista_divisores1.append(divisor)
        #         temp_var1 /= divisor
        #     else:
        #         counter += 1
        #         divisor = lista_primos_var1[counter]
        #
        # lista_primos_var2 = cria_lista_numeros_primos_ate_n(var2)
        #
        # print("lista_primos_var2:", lista_primos_var2)
        #
        # divisor = lista_primos_var2[1]
        # counter = 0
        # lista_divisores2 = list()
        # temp_var2 = var2
        #
        # while temp_var2 != 1:
        #     if temp_var2 % divisor == 0:
        #         lista_divisores2.append(divisor)
        #         temp_var2 /= divisor
        #     else:
        #         counter += 1
        #         divisor = lista_primos_var2[counter]

        print("LISTA DIVISORES 1: ", lista_divisores1)
        print("LISTA DIVISORES 2: ", lista_divisores2)


        lista_interseccao_divisores = intersection(lista_divisores1, lista_divisores2)
        # lista_interseccao_divisores = set(lista_divisores1).intersection(set(lista_divisores2))

        print("lista_interseccao_divisores:", lista_interseccao_divisores)

        return multiply(lista_interseccao_divisores)


# a = 12
# b = 8
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 4

# a = 12
# b = 24
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 12

# CASO DE ERRO! ARRUMAR NO insersection()
# a = 120
# b = 150
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 30

# a = 180
# b = 36
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 36

# a = 180
# b = 252
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 36

# a = 180
# b = 108
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 36

# a = 3
# b = 4
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 1

# a = 10
# b = 11
# print("MDC({},{}) = {}".format(a, b, mdc(a, b)))  # = 1



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
