# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:49:51 2021

@author: Gonzalo
"""

#your_name = input ("Give me your name now or else !!!!!!!! ")
#print (your_name[6:])     

school_sux = "coral gables senior high"
print (school_sux[9])


"""
print out from the tenth letter 
to the end of the stirng 

"""
print (school_sux[9:])
#print out the second to the fifth letter
print (school_sux[1:4])
#in reverse 
print (school_sux[::-1])
#print every other letter 
print(school_sux[::2])
#the length if the sring 
L = len(school_sux)
print("size of the string is: ", L)

print ("where is the first space in the string ?")
print(school_sux.index(" "))
print ("where is the second space in the string ?")
print(school_sux.index(" " ,6))
print(school_sux[:5])
print(school_sux[6:12])

month = input ("Birth month: ")
day = input ("birth day")
year = input("birth year")
n = input ("your first and last name: ")

space = n.index(" ")
initials = n[0] + n[space + 1]
print("your Gables  password is  ")
print(month + day + year + initials)