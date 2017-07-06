def fatorial(x):
    
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)
