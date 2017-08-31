# -*- coding: utf-8 -*-

class Parent:        # Визначити батьківський клас
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # Визначити дитячий клас
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # Примірник дитини
c.childMethod()      # Дитина називає його метод
c.parentMethod()     # Викликає метод батьків
c.setAttr(200)       # Знову викликати метод батьків
c.getAttr()          # Знову викликати метод батьків