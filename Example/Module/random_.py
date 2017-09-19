# -*- coding: utf-8 -*-

import random

def q1():
    g = ['q','w','e']
    g1 =[1,2]
    List = [1,2,3,4,5,6,7,8,9]
    e =random.seed(20)
    e1=random.random()
    e2=random.uniform(0, 20)
    e3=random.randint(0, 3)
    e4=random.choice(g)
    e5=random.randrange(1, 90, 2)
    e6=random.shuffle(List)
    print(e, e1, e2, e3, e4, e5, List)
    

q1()