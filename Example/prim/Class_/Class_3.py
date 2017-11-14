# -*- coding: utf-8 -*-

class Parent:
    def myMetod(self):
        print("calling parent metod")
        x = print("Ok")
        
class Child(Parent):
    def myMetods(self):
        print("Calling child metod")
        print(x)
        
c = Child()
c.myMetods()