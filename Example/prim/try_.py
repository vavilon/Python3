# -*- coding: utf-8 -*-

def prim():
    try:
        fh = open("testfile", "w")
        fh.write("This is my test file for exception handling")
    except IOError:
        print("Erroe: can\ ")
    else:
        print("Write content in the file")
        fh.close()
        
def prim_():
    try:
        fh = open("testfile", "w")
        fh.write("This is my test file for")
    finally:
        print("Error: can ")
        fh.close()
        
def prim_1():
    try:
        fh = open("testfile", "w")
        try:
            fh.write("This is my test file")
        finally:
            print("Going to close the file")
            fh.close()
    except IOError:
        print("Error: can")
        
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
prim()
prim_()
prim_1()