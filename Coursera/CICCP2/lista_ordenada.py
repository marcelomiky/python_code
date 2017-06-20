def ordenada(list):
    
    flag = True
    
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            flag = False
    
    return flag
