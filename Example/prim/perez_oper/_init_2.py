# -*- coding: utf-8 -*-

class Bass:
    def __init__(self, arg = "argument"):
        self.arg = arg
        
class Der(Bass):
    pass

b = Bass()
print(b.arg)

bb = Der()
print(bb.arg)

es = Der("arguments char")
print(es.arg)