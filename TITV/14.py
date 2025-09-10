# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 21:11:46 2025

@author: My PC
"""

x = int(input(" Nhap so bat ki :"))

#vd1
if x >= 0:
   print( x ,"la so duong")
   
#vd2 
if x % 2 ==0:
    print(x , " la so chan ")
else:
        print(x , " x la so le ")
   
    
#vd3
if x >= 9:
    print(" Xep loai : Xuat Sac")
elif x >= 8:
    print(" Xep loai :  Gioi ")
elif x >= 7:
 print(" Xep loai : Kha ")
else:
    print(" Xep loai : Trung Binh")
    
    
print(" Ket Thuc Chuong Trinh")

# Nhập điểm từ người dùng
x = float(input("Nhập điểm (0 - 10): "))

# Kiểm tra hợp lệ
if x < 0 or x > 10:
    print("Điểm không hợp lệ! Vui lòng nhập số từ 0 đến 10.")
else:
    # Xếp loại bằng chữ và mô tả
    if x >= 9:
        grade = "A"
        mota = "Xuất Sắc"
    elif x >= 8:
        grade = "B"
        mota = "Giỏi"
    elif x >= 7:
        grade = "C"
        mota = "Khá"
    elif x >= 5:
        grade = "D"
        mota = "Trung Bình"
    else:
        grade = "F"
        mota = "Yếu"

    # In kết quả
    print(f"Điểm của bạn: {x}")
    print(f"Xếp loại: {mota} (Grade {grade})")

print("Kết thúc chương trình")

