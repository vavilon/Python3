# -*- coding: utf-8 -*-

import time

def prim():
    
    print("prim--",time.localtime());
    
def prim_1():
    localtime = time.asctime( time.localtime(time.time()) )
    print ("prim_1--","Local current time :", localtime)

def prim_2():
    print (time.asctime( time.localtime(time.time()) ))
    

prim()
prim_1()
prim_2()