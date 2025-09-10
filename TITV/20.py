# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 09:45:28 2025

@author: My PC
"""
#
a = 10 
print(type(a))

# Cong chuoi
s1 = "abc"
s2 = "def"
s3 = s1 + "" +s2
print(s3)

#Chuoi nhieu dong
chuoi_nhiu_dong= '''
d1
d2
d2
'''
print(chuoi_nhiu_dong)

# Lap lai chuoi
chep_phat = "ABCDEFGH"
chep_phat_10 = chep_phat*10
print(chep_phat_10)
#Kiem tra chuoi co thuoc khac
chuoi_1 = " Xin Chao TITV"
chuoi_2 = "TITV"
chuoi_3 = "ZXV"
if chuoi_2 in chuoi_1:
    print("Chuoi2_la con chuoi_1")
else:
        print("Chuoi_2 khong phai la con chuoi_1")
if chuoi_3 in chuoi_1 :
            print("Chuoi_3 la con chuoi_1")
else:
                print("Chuoi_3 khong la con chuoi_1")


#Viet hoa chu dau chuoi 
s = "hom nay troi dep qua"
s = str.capitalize(s)
print(s)

#Viet hoa toan bo chuoi 
s = s.upper()
print(s)
#Viet nguoc
s = s.lower()
print(s)

# Tim va Dem so luong chuoi con 
s1 = "A B C D E F G H E E J K L"


print(s1.find("M")) # Tra ve tru 1 neu khong co
print(s1.find("B"))
print(s1.count("F"))


# Ham Thay The 
s1 = s1.replace("A" , "a")
print(s1)
# Cat chuoi thanh 1 list
s1 = s1.split(" ")
print(s1)

print(s1[1:3])