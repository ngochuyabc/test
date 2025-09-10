# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 20:46:19 2025

@author: My PC
"""

# Vong lap tu 0 -> n-1
n = int(input("Nhap n :"))
for i in range(n):
    print(i)
    
# Tong tu 0 -> n
n = int(input("Nhap n : "))
tong = 0
for i in  range(n+1):
    tong+=i
    print("tong = :" , tong)
    
    
#Vong lap for , co buoc tang tuy chinh 
for i in range(0 , 10 , 2):
    print(i)
    
    
for i in range(10 , 0 , -1):
    print(i)


colors = ["a","b", "c"]
# Vong lap for duyet cac phan tu cua list
for color in colors:
    print(color)
    
for i in range(len(colors)):
    print(colors[i])