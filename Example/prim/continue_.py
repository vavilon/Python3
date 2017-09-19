# -*- coding: utf-8 -*-

def p1():
    for i in 'hello world':
        if i == 'o':
            continue
        print(i * 2, end='')
def p2():
    for letter in 'Django':
        if letter == 'd':
            continue
        print("create: ", letter)
 
     
        
p1()
p2()