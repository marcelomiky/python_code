print("Digite uma sequência de valores termiada por zero.")

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor a ser somado:"))
    soma += valor
    
print("A soma dos valores digitados é: ", soma)
