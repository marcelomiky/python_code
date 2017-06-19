x = int(input('Insira um número inteiro positivo:'))

divisores = 0

for i in range(1, x):
    if x % i == 0:
        divisores += 1

if divisores >= 2:
    print('não primo')
else:
    print('primo')
