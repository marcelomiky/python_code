def incomodam(n):
    
    if type(n) != int or n <= 0:
        return ''
    else:
        s1 = 'incomodam '
        return s1 + incomodam(n - 1)

def elefantes(n):
    
    if type(n) != int or n <= 0:
        return ''
    if n == 1:
        return "Um elefante incomoda muita gente"
    else:
        return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente" if n % 2 > 0 else "muito mais") +  "\r\n"
