# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 09:37:19 2025

@author: My PC
"""
"""
emtylist =["A", "B", "C", "D"]
print(emtylist[0])
print(emtylist[1:3])
print(emtylist[0:2])
"""

emtyList = ["A","B","C","D","E","F"]

# Nối - Thêm vào sau
emtyList.append(5)
print(emtyList)

# Truy xuất phần tử cuối 
print(emtyList[-1])



# Sap xep tu lon den be
emtyList1 = [1,3,2,6,8,4,0,1,1]
emtyList1.sort(reverse=True)
print(emtyList1)
# Dem so luong phan tu trong list
print(len(emtyList1))

# Sap xep tu be den lon
emtyList1.sort()
print(emtyList1)

#Them vao vi tri bat ki trong list
emtyList1.insert(2, 9)
print(emtyList1)

#List co thu tu , vi tri cac phan tu duoc danh dau tu 0 , tu trai sang phai 
print(emtyList[1])

#Dem so luong phan tu thoa dieu kien 
print(" ",emtyList1.count(1))

# Xoa phan tu ra khoi list bang gia tri
emtyList1.remove(3)
print(emtyList1)
emtyList.remove("A")
print(emtyList)

#Kiem tra phan tu co ben trong List :in
if "B" in emtyList:
    emtyList.remove("B")
    print(emtyList)
#Xoa phan tu ra khoi list bang vi tri
emtyList.pop(4)
print(emtyList)

# Doi nguoc vi tri
emtyList2 = ["S", "V", "N","Q", "W"]
emtyList2.reverse()
print(emtyList2)
# Sap xep lai 
emtyList2.sort()
print(emtyList2)

#Xoa sach du lieu 
emtyList2.clear()
print(emtyList2)