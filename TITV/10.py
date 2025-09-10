# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:58:23 2025

@author: My PC
"""

print(" Vi du ve toan tu so sanh :")
x = int(input("x = "))
y = int(input("y = "))


# True or fALE
print("{0}<{1} la {2}".format(x, y , x < y))
print("{0}>{1} la {2}".format(x, y , x > y))
print("{0}=={1} la {2}".format(x, y , x == y))
print("{0}!={1} la {2}".format(x, y , x != y))
print("{0}>={1} la {2}".format(x, y , x >= y))
print("{0}<={1} la {2}".format(x, y , x <= y))


print(" Vi du ve toan tu logic :")
z = int(input(" z = "))
print((x<y) and (y<z) ) #(10<15) and ( 15<8) -> F
print((x<y)  or (y<z)) # (10<15) or (15<8) -> T
print(( not x<y)  ) 

print("{0} < {1} and {2}<{3} = {4}".format(x,y,y,z, x<y and y<z))
print("{0} < {1} and {2}<{3} = {4}".format(x,y,y,z, x<y or y<z))
print("not {0} < {1} = {2}".format(x,z, not x < y))