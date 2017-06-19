qtd = int(input("Insira um número inteiro positivo:"))

i = 1

while qtd > 0:
    if i % 2 != 0:
        print(i)
        qtd -= 1
    i += 1   
