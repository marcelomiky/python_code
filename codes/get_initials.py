def get_initials(name):
    
    initials = list()
    
    name_in_list = name.split()
    
    initials_list = [i[0] for i in name_in_list]
    
    initials_string = ''
    
    for j in initials_list:
        initials_string += j

    return initials_list, initials_string