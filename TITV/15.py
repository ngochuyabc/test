# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 23:03:58 2025

@author: My PC
"""

# import thu vien 
import math 

# Nhap du lieu 
print(" Giai Phuong Trinh ax^2+bx+c= 0")
a = float(input("Nhap so a :"))
b = float(input("Nhap so b :"))
c = float(input("Nhap so c :"))

print("{0}x^2 + {1}x + {2}= 0".format(a,b,c)) # Hien thi lai phuong trinh ma nguoi dung da nhap
if a!= 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print(" Phuong trinh vo nghiem")
    elif delta ==0:
        x = -b/(2*a)
        print("Phuong trinh co nghiem kep x1=x2=" ,x)
    elif delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet x1={0}, x2={1}" .format (x1, x2))
else:
    print(" Khong phai phuong trinh bac 2")
    
#vd2

import math
print(" ax^2 +bx +c=0")
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))
print ("{0}x^2+{1}x+{2}=0".format(a,b,c))

if a!= 0 :
    delta = b**2-4*a*c
    if delta < 0:
        print("pt vo no")
    elif delta ==0:
        x = -b/(2*a)
        print("pt co nghiem kep x1=x2=", x)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet x1={0}, x2={1}" .format (x1, x2))
else:
            print(" Khong phai phuong trinh bac 2")
            
        
        
        

    
    
    
