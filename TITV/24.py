# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 13:31:48 2025

@author: My PC
"""

number = ( 1 , 2 ,3 ,4 , 5 ,6 ,7 ,8 ,9 ,10)
gioiTinh = ( "Nam" , "Nu")
chucai = ( " A", "C" , "B", "D" ,"V", "F", "E")
print(gioiTinh[0])
print(number[0:4])
# Gia tri phan tu cua Tuple khomg the thay doi 
# vd : number[0] = 11
#list = [ 1,2,3,4,5]
#list[0]= 13
#print(list)


# Cac thao tac voi Tuple
#1. Cong 2 tuple
y = ( 1,2,3)+(4,5,6)
print (y)
#2 . Duyet phan tu ben trong bang vong lap 
for x in gioiTinh:
    print(x)
    
#3.Nhan hai tuple
y = (1,2,3)*2
print(y)
# 4 Dung in de kiem tra xem 1 phan tu co ton tai ben trong bo tuple hay khong
print("Khac" in gioiTinh) 
print("Nam" in gioiTinh)

#5 Lay ra do dai , so luong phan tu 
x = len(number)
print (x)
#6 Dem so luong xuat hien 
print(number.count("11"))
#7 Min , Max , Sum
print(min(number))
print(max(number))
print(sum(number))

#8 Sap xep tuple va chuyen ve list
list1=sorted(chucai)
print(list1)