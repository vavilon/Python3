# -*- coding: utf-8 -*-
def pri():
    i = 4

    while i < 10:
        print(i)
        i = i + 1
        
def pri1():
    y =2
    while y <= 4:
        print(y ** 2)
        y += 1
        
def pri2():
    f = 1
    while f <= 10:
        print(f)
        f += 1
    else:
        print("cikl end, f=",f)
        
def pri3():
    a = int(input())
    while a != 0:
        if a < 0:
            print('Встретилось отрицательное число', a)
            break
        a = int(input())
    else:
        print('Ни одного отрицательного числа не встретилось')
        
pri()
pri1()
pri2()
pri3()