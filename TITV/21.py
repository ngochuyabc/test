# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 21:01:18 2025

@author: My PC
"""

n = -1 

while  ( n<=0):
    n = int (input("Nhap vao n : "))
    
i = 0 
tong = 0 
while (i<=n):
    tong+=i # Tong = Tong + i 
    i+=1 # i = i + 1
    print("Tong =", tong)
    

j = 0 
while (j<=10):
    print(j," - Ben trong vong lap")
    j+=1
else:
    print(j, " Ben ngoai vong lap")
    
j = 0 
while (j<=10):
    print(j," - Ben trong vong lap")
    j+=1
    if j>=5:
        break
else:
    print(j, " Ben ngoai vong lap")