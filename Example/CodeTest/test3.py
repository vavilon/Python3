# -*- coding: utf-8 -*-

class Base:
    def __init__(self, arg1 = "argument one"):
        self.arg1 = arg1
    
        
class Derived(Base):
    pass
    
b = Base()
print (b.arg1)
 
d = Derived()
print (d.arg1)
 
e = Derived("argument changed!")
print (e.arg1)