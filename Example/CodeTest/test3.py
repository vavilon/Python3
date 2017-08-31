# -*- coding: utf-8 -*-

def ifs():
    if 4 < 2:
        print("@")
    elif 4<1:
        print("!")
    else:
        print("E")
        
def whiles():
    e = 2
    while e < 5:
        print(e)
        e = e + 1
        
def con():
    for i in "my friend":
        if i == 'o':
            continue
        print(i*2, end= "")
        
def fors():
    for i in 'hels':
        print(i*2, end='')
        
ifs()
whiles()
con()
fors()