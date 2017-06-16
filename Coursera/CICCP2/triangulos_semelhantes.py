class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# https://stackoverflow.com/questions/961048/get-class-that-defined-method
    def semelhantes(self, Triangulo):
        
        list1 = []
        
        for arg in self:
            list1.append(arg)
            
        list2 = []
        
        for arg in Triangulo:
            list2.append(arg)
        
        
        for i in list2:
            print(i)
        
