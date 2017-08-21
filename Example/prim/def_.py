# -*- coding: utf-8 -*-

def hello():
    print("def Ok")
    
def add(x, y):
    return x + y

def newfunc(n):
    def func(z):
        return z + n
    return func

#print(hello())
#print(add(1, 10))
#new = newfunc(10)
#print(new(12))