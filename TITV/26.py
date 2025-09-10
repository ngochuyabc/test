import random

thung = set()

while True:
    print("\n.............Menu............")
    print("Vui lòng chọn chức năng:")
    print("1 - Thêm số điện thoại dự thưởng")
    print("2 - Xóa số điện thoại dự thưởng")
    print("3 - Quay số ngẫu nhiên")
    print("4 - Hiển thị thùng")
    print("5 - Thoát")
    
    chon = int(input("Chọn chức năng: "))

    if chon == 1:
        ma = int(input("Nhập số điện thoại: "))
        thung.add(ma)
        print("Đã thêm:", ma)
        
    elif chon == 2:
        ma = int(input("Nhập số muốn xóa: "))
        if ma in thung:
            thung.discard(ma)
            print("Đã xóa:", ma)
        else:
            print("Số này không có trong thùng.")
            
    elif chon == 3:
        if thung:
            ma_trung = random.choice(list(thung))
            print("Số trúng thưởng là:", ma_trung)
            if ma_trung in thung:
                thung.remove(ma_trung)
        else:
            print("Thùng rỗng!")
            
    elif chon == 4:
        print("Thùng hiện tại:", thung)
        
    elif chon == 5:
        print(" Kết thúc")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
