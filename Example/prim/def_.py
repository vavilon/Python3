# -*- coding: utf-8 -*-

def hello():
    print("def Ok")
    
def add(x, y):
    return x + y

def newfunc(n):
    def func(z):
        return z + n
    return func

def prim(str):
    print(str)
    return

def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

printinfo( age = 50, name = "miki printinfo" )
printinfo( name = "miki printinfo" )

prim("prim")
#print(hello())
#print(add(1, 10))
#new = newfunc(10)
#print(new(12))