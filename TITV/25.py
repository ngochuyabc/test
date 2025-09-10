# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 14:19:33 2025

@author: My PC
"""
# Set là 1 kiểu dữ liệu tích hợp sẵn trong python dùng để  lưu trữ các tập hợp dữ liệu
# Là tập hợp khôg có thứ tự , giá trị không được trùng lặp nhau , không thể thay đổi giá trị , nhưng có thể xóa và thêm các mục mới 

# Định nghĩa 
list = { "A", "B", "C", "D","E","F","G"}
print(list) 

# Duyet ds phan tu 
for x in list :
    print(x)
    
# Them phan tu vao list
#add
list.add("K")
print(list)
list.add("Huy")
print(list)
#update
list1= {"M","N","X"}
list.update(list1)
print(list)
#Xoa phan tu
#remove : neu phan tu khong ton tai se phat sinh loi
list.remove("Huy")
print(list)
list.remove("Q")
print(list)
# phan tu kgong ton tao khong bao loi 
list.discard("Q")
print(list)
#xoa phan tu dau tien 
list.pop()
print(list)
# xoa toan bo phan tu
list.clear()
print()
# xoa chuoi 
del list
print()

