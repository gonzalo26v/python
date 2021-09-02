# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:56:14 2021

@author: Gonzalo
"""

day = "Thursday"
print (type(day))
day = 32.5
print (type(day))
day = 19
print(type(day))
day = 3j
print(type(day))


expenses1 = float(input("How much did you spend on sunday ? "))
expenses2 = float(input("How much did you spend on monday ? "))
#toatl $ is a bad variable name because of $
total = (expenses1) + (expenses2)
print ("you spent : $" + "{:.2f}".format(total))

#casting
x= int (1)
y = int (2.8)
z= int ("3")
print(x, end="")
print(y, end = '')
print(z,end = "")

x = float(1)
y = float (2.8)
z = float ("3")
w = float ("4.2")
print(x, end="")
print(y, end = '')
print(z,end = "")
print(w, end = "")

x= str ("s1")
y = str (2)
z= str (3.8)
print (x)
print (y)
print (z)

x = complex (5)
print (x)
