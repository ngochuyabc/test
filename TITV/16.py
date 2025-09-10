# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:24:02 2025

@author: My PC
"""
"""
Nhập 3 điểm trên trục tọa độ Oxy
1. Xác định 3 điểm có tạo thành tam giác không
2. Nếu tạo thành tam giác:
    2.a Xuất ra chu vi của tam giác
    2.b Xuất ra diện tích của tam giác 
"""

import math 

xA = float(input(" Nhap xA :"))
yA = float(input(" Nhap yA :"))
xB = float(input(" Nhap xB :"))
yB = float(input(" Nhap yB :"))
xC = float(input(" Nhap yC :"))
yC = float(input(" Nhap yC :"))



ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
bc = math.sqrt((xC-xA)**2 + (yC-yB)**2)
ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)

#Kiem tra 
if ab + bc > ac and bc + ac > ab and ab + ac > bc :
    print(" La Tam Giac ")
# Tinh Chu Vi  
    cv = ab + bc +ac   
    print(" Chu vi la :" , cv)
# Tinh Dien Tich
    p = cv/2
    print("Nua chu vi tam giac la :", p)
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("Dien tich tam giac la :", s)
    
else:
       print ("Khong Phai La Tam Giac ")
        
