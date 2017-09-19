# -*- coding: utf-8 -*-

#Задание множеств

def rt():
    a = {1,2,3}
    a = set('12345')
    print(a)
    
def rt1():
    a = {1,2,3}
    b = {3,2,3,1}
    print(a == b)
    
def rt2():
    primes={2,3, 5, 7, 11}
    for num in primes:
        print(num)
        
def rt3():
    a = {1, 2, 3}
    print(1 in a, 4 not in a)
    a.add(4)
rt()
rt1()
rt2()
rt3()