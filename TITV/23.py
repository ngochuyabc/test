# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 22:07:43 2025

@author: My PC
"""
#for
for i in range (0,10):
    print(i)
#for - break
for i in range (0,10):
    print(i)
    if ( i > 5):
        break 
    #while
n = 100
while   n > 0:
 print (n)
 n = n // 2
 
 #while - break
n = 100 
while n > 0 :
    print (n)
    n = n // 2 
    if n < 50 :
        break
# long nhau 
for i in range(2,10):
    print (" Bang Cuu Chuong", i)
    for j in range(1,11):
        print ( "{0}*{1}= {2}".format( i , j , i*j))
        if j > 5:
            break
        
# continue 
for i in range(0,10):
    if ( i%2==1):
        continue
    print(i)


    
    
 