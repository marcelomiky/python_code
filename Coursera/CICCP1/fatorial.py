n = int(input("Insira um número natural n:"))

i = 1
fat = 1

while i <= n:
    fat *= i
    i += 1

print(fat)
