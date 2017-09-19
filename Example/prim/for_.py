# -*- coding: utf-8 -*-

def t1():
    for i in 'hello world':
        print(i* 2, end='')
    
def t2():
    words = [' cat', 'window', 'def']
    for w in words:
        print(w, len(w))
        
t1()
t2()
