from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")
root = tree.getroot()

# 1. Lấy tất cả sinh viên
print("Tất cả sinh viên:")
for s in root.xpath("//student"):
    print(etree.tostring(s, pretty_print=True, encoding='unicode'))

# 2. Liệt kê tên tất cả sinh viên
print("\nTên tất cả sinh viên:")
print(root.xpath("//student/name/text()"))

# 3. Lấy tất cả id sinh viên
print("\nTất cả ID sinh viên:")
print(root.xpath("//student/id/text()"))

# 4. Lấy ngày sinh của sinh viên có id = SV01
print("\nNgày sinh SV01:")
print(root.xpath("//student[id='SV01']/date/text()"))

# 5. Lấy các khóa học
print("\nCác khóa học:")
print(root.xpath("//enrollment/course/text()"))

# 6. Lấy toàn bộ thông tin sinh viên đầu tiên
print("\nThông tin sinh viên đầu tiên:")
print(etree.tostring(root.xpath("//student[1]")[0], pretty_print=True, encoding='unicode'))

# 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'
print("\nMã sinh viên học Vatly203:")
print(root.xpath("//enrollment[course='Vatly203']/studentRef/text()"))

# 8. Tên sinh viên học môn 'Toan101'
print("\nTên sinh viên học Toan101:")
print(root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"))

# 9. Tên sinh viên học môn 'Vatly203'
print("\nTên sinh viên học Vatly203:")
print(root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"))

# 10. Ngày sinh SV01
print("\nNgày sinh SV01:")
print(root.xpath("//student[id='SV01']/date/text()"))

# 11. Tên và ngày sinh sinh viên sinh năm 1997
print("\nTên và ngày sinh sinh viên sinh năm 1997:")
for s in root.xpath("//student[starts-with(date, '1997')]"):
    print(s.xpath("name/text()")[0], "-", s.xpath("date/text()")[0])#Giữ lại những <student> có <date> bắt đầu bằng "1997 Lấy <name> và <date> của từng sinh viên
# 12. Tên sinh viên sinh trước năm 1998
print("\nTên sinh viên sinh trước 1998:")
print(root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()")) #cắt chuỗi,substring(date, 1, 4) → lấy ra phần “năm” của ngày sinh

# 13. Đếm tổng số sinh viên
print("\nTổng số sinh viên:", root.xpath("count(//student)")) #count: đếm

# 14. Sinh viên chưa đăng ký môn nào (nếu có thêm SV mới)
print("\nSinh viên chưa đăng ký môn nào:")
print(root.xpath("//student[not(id = //enrollment/studentRef)]/name/text()"))

# 15. Phần tử <date> anh em ngay sau <name> của SV01
print("\nDate sau name của SV01:")
print(root.xpath("//student[id='SV01']/name/following-sibling::date/text()")) #following-sibling:: Lấy các phần tử cùng cấp, đứng sau node hiện tại

# 16. Phần tử <id> anh em ngay trước <name> của SV02
print("\nID trước name của SV02:")
print(root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()")) #preceding-sibling::Lấy các phần tử cùng cấp, đứng trước node hiện tại
                                                                            #child::	Lấy phần tử con trực tiếp
                                                                                #parent::	Lấy phần tử cha
                                                                                #descendant::	Lấy phần tử con ở mọi cấp  
# 17. Tất cả <course> cùng enrollment với SV03
print("\nCourse của SV03:")
print(root.xpath("//enrollment[studentRef='SV03']/course/text()"))

# 18. Sinh viên có họ 'Trần'
print("\nSinh viên họ Trần:")
print(root.xpath("//student[starts-with(name, 'Trần')]/name/text()"))

# 19. Năm sinh của SV01
print("\nNăm sinh SV01:")
print(root.xpath("substring(//student[id='SV01']/date, 1, 4)"))
