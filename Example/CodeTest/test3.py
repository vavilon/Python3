# -*- coding: utf-8 -*-

class S:
    def __init__(self, name, cat, n=0):
        self.name = name
        self.car = cat
        #self.nums = n
        
    def jr(self, name, cat, n):
        if n <=0:
            self.where = "no"
        else:
            self.where = "yes"
            
m1 = S("ni", "k", 50)
            
#S.jr()
print(m1.car)