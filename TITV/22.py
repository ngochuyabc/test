# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 09:52:01 2025

@author: My PC
"""
# Nhap n ( n > 0 )
n = -1
while (n <= 0) :
    n = int(input(" Nhap vao n > 0:"))
    
# Chuyen tu thap phan sang nhi phan
x = n 
ketqua = " "
while (n  > 0):
    ketqua = str(n%2) + ketqua 
    print(" n%2 = ", n % 2)
    n = n //2
    print("n = ", n )
    
print(" Ket qua : ", ketqua )
    
