largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:
    for i in range(largura):
        print("#", end = '')
    print()
    altura -= 1 
