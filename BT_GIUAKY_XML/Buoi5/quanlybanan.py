from lxml import etree

# Đọc file XML
tree = etree.parse("quanlybanan.xml")

print("===== KẾT QUẢ TRUY VẤN XPATH =====")

# 1. Lấy tất cả bàn
ban = tree.xpath("//BAN")
print("1. Tất cả bàn:", len(ban))

# 2. Lấy tất cả nhân viên
nhanvien = tree.xpath("//NHANVIEN")
print("2. Tất cả nhân viên:", len(nhanvien))

# 3. Lấy tất cả tên món
ten_mon_all = tree.xpath("//MON/TENMON/text()")
print("3. Tất cả tên món:", ten_mon_all)

# 4. Lấy tên nhân viên có mã NV02
ten_nv02 = tree.xpath("//NHANVIEN[MANV='NV02']/TENNV/text()")
print("4. Tên nhân viên NV02:", ten_nv02)

# 5. Lấy tên và số điện thoại của nhân viên NV03
ten_nv03 = tree.xpath("//NHANVIEN[MANV='NV03']/TENNV/text()")
sdt_nv03 = tree.xpath("//NHANVIEN[MANV='NV03']/SDT/text()")
print("5. NV03 - Tên:", ten_nv03, ", SĐT:", sdt_nv03)

# 6. Lấy tên món có giá > 50,000
ten_mon_gt50k = tree.xpath("//MON[GIA>50000]/TENMON/text()")
print("6. Món giá > 50.000:", ten_mon_gt50k)

# 7. Lấy số bàn của hóa đơn HD03
so_ban_hd03 = tree.xpath("//HOADON[SOHD='HD03']/SOBAN/text()")
print("7. Số bàn của hóa đơn HD03:", so_ban_hd03)

# 8. Lấy tên món có mã M02
ten_mon_m02 = tree.xpath("//MON[MAMON='M02']/TENMON/text()")
print("8. Tên món M02:", ten_mon_m02)

# 9. Lấy ngày lập của hóa đơn HD03
ngaylap_hd03 = tree.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()")
print("9. Ngày lập HD03:", ngaylap_hd03)

# 10. Lấy tất cả mã món trong hóa đơn HD01
ma_mon_hd01 = tree.xpath("//HOADON[SOHD='HD01']/CTHD/CT/MAMON/text()")
print("10. Mã món trong HD01:", ma_mon_hd01)

# 11. Lấy tên món trong hóa đơn HD01
ten_mon_hd01 = tree.xpath("//MON[MAMON=//HOADON[SOHD='HD01']/CTHD/CT/MAMON]/TENMON/text()")
print("11. Tên món trong HD01:", ten_mon_hd01)

# 12. Lấy tên nhân viên lập hóa đơn HD02
ten_nv_hd02 = tree.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV]/TENNV/text()")
print("12. Tên nhân viên lập HD02:", ten_nv_hd02)

# 13. Đếm số bàn
so_ban = tree.xpath("count(//BAN)")
print("13. Tổng số bàn:", int(so_ban))

# 14. Đếm số hóa đơn lập bởi NV01
so_hd_nv01 = tree.xpath("count(//HOADON[MANV='NV01'])")
print("14. Số hóa đơn lập bởi NV01:", int(so_hd_nv01))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
ten_mon_ban2 = tree.xpath("//MON[MAMON=//HOADON[SOBAN=2]/CTHD/CT/MAMON]/TENMON/text()")
print("15. Món trong hóa đơn của bàn 2:", ten_mon_ban2)

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
nv_ban3 = tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN=3]/MANV]/TENNV/text()")
print("16. Nhân viên phục vụ bàn 3:", nv_ban3)

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
hd_nv_nu = tree.xpath("//HOADON[MANV=//NHANVIEN[GIOITINH='Nu']/MANV]/SOHD/text()")
print("17. Hóa đơn do nhân viên nữ lập:", hd_nv_nu)

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
nv_ban1 = tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN=1]/MANV]/TENNV/text()")
print("18. Nhân viên phục vụ bàn 1:", nv_ban1)

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần
mon_gtr1 = tree.xpath("//MON[MAMON=//CTHD/CT[SOLUONG>1]/MAMON]/TENMON/text()")
print("19. Món được gọi >1 lần:", mon_gtr1)

# 20. Lấy tên bàn + ngày lập hóa đơn HD02
ban_ngay_hd02 = tree.xpath("concat(//BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN/text(), ' - ', //HOADON[SOHD='HD02']/NGAYLAP/text())")
print("20. Bàn và ngày lập HD02:", ban_ngay_hd02)
