players = []

def tinh_diem(tran, ban, ktao):
    return tran + ban*3 + ktao*2

def xep_loai(diem):
    if diem < 15:
        return "Cần thanh lý"
    elif diem < 30:
        return "Dự bị"
    elif diem < 50:
        return "Trụ cột"
    else:
        return "Ngôi sao"

def hien_thi():
    if not players:
        print("Danh sách trống!")
        return

    print(f"{'Mã':<6}{'Tên':<20}{'Trận':<6}{'Bàn':<6}{'KT':<6}{'Điểm':<6}{'Loại'}")
    for p in players:
        print(f"{p['ma']:<6}{p['ten']:<20}{p['tran']:<6}{p['ban']:<6}{p['ktao']:<6}{p['diem']:<6}{p['loai']}")

def them():
    ma = input("Nhập mã: ").strip()

    if ma == "":
        print("Không được để trống!")
        return

    for p in players:
        if p["ma"] == ma:
            print("Mã bị trùng!")
            return

    ten = input("Nhập tên: ").strip()
    if ten == "":
        print("Tên không được trống!")
        return

    try:
        tran = int(input("Số trận (0-50): "))
        if tran < 0 or tran > 50:
            print("Số trận không hợp lệ!")
            return

        ban = int(input("Bàn thắng: "))
        ktao = int(input("Kiến tạo: "))

        if ban < 0 or ktao < 0:
            print("Không được âm!")
            return

    except:
        print("Nhập sai định dạng!")
        return

    diem = tinh_diem(tran, ban, ktao)
    loai = xep_loai(diem)

    player = {
        "ma": ma,
        "ten": ten,
        "tran": tran,
        "ban": ban,
        "ktao": ktao,
        "diem": diem,
        "loai": loai
    }

    players.append(player)
    print("Thêm thành công!")

def cap_nhat():
    ma = input("Nhập mã cần sửa: ")

    for p in players:
        if p["ma"] == ma:
            try:
                tran = int(input("Trận mới: "))
                ban = int(input("Bàn mới: "))
                ktao = int(input("KT mới: "))
            except:
                print("Sai dữ liệu!")
                return

            p["tran"] = tran
            p["ban"] = ban
            p["ktao"] = ktao

            p["diem"] = tinh_diem(tran, ban, ktao)
            p["loai"] = xep_loai(p["diem"])

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy!")
def xoa(): 
    

while True:
    print("\n===== MENU =====")
    print("1. Hiển thị")
    print("2. Thêm")
    print("3. Cập nhật")
    print("4. Xóa")
    print("5. Tìm kiếm")
    print("6. Thống kê")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        hien_thi()
    elif chon == "2":
        them()
    elif chon == "3":
        cap_nhat()
    elif chon == "4":
        xoa()
    elif chon == "5":
        tim_kiem()
    elif chon == "6":
        thong_ke()
    elif chon == "0":
        print("Tạm biệt!")
        break
    else:
        print("Chọn sai!")