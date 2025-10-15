from lxml import etree
import mysql.connector
from mysql.connector import Error

# ---  Đọc và kiểm tra XML với XSD ---
xml_file = "catalog.xml"
xsd_file = "catalog.xsd"

try:
    # Đọc file XML và XSD
    xml_doc = etree.parse(xml_file)
    xsd_doc = etree.parse(xsd_file)
    schema = etree.XMLSchema(xsd_doc) # tạo đối tượng kiểm tra XMLSchema

    # Kiểm tra hợp lệ
    if not schema.validate(xml_doc): # kiểm tra XML có tuân theo cấu trúc trong XSD
        print(" XML không hợp lệ với XSD!")
        for error in schema.error_log:
            print(f" - Lỗi dòng {error.line}: {error.message}")
        exit(1)
    else:
        print(" XML hợp lệ với XSD!")

except Exception as e:
    print(f" Lỗi khi đọc hoặc kiểm tra XML/XSD: {e}")
    exit(1)


# ---  Kết nối MySQL ---
try:
    conn = mysql.connector.connect( #tạo kết nối đến database.
        host="localhost",
        user="root",
        password="",       
        database="shopdb"  
    )

    if conn.is_connected(): #kiểm tra trạng thái kết nối
        print(" Kết nối MySQL thành công!")
    cursor = conn.cursor()

except Error as e:
    print(f" Lỗi kết nối MySQL: {e}")
    exit(1)

# ---  Dùng XPath để lấy dữ liệu ---
root = xml_doc.getroot()

categories = root.xpath("//categories/category") #lấy tất cả <category> nằm trong <categories>
products = root.xpath("//products/product") #lấy tất cả <product> nằm trong <products>

# ---  Insert hoặc Update dữ liệu ---
try:
    # --- Bảng Categories ---
    for c in categories:
        cid = c.get("id")
        cname = c.text.strip() if c.text else ""

        cursor.execute("""
            INSERT INTO Categories (id, name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """, (cid, cname)) #ON DUPLICATE KEY UPDATE → nếu id đã tồn tại → chỉ cập nhật tên (name), không thêm dòng mới.

    # --- Bảng Products ---
    for p in products:
        pid = p.get("id")
        pref = p.get("categoryRef")
        name = p.findtext("name")
        price_node = p.find("price")
        price = float(price_node.text)
        currency = price_node.get("currency")
        stock = int(p.findtext("stock"))

        cursor.execute("""
            INSERT INTO Products (id, name, price, currency, stock, categoryRef)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                price = VALUES(price),
                currency = VALUES(currency),
                stock = VALUES(stock),
                categoryRef = VALUES(categoryRef)
        """, (pid, name, price, currency, stock, pref))

    conn.commit()
    print("Dữ liệu đã được chèn hoặc cập nhật thành công!")

except Error as e:
    conn.rollback()
    print(f" Lỗi khi chèn dữ liệu: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
        print(" Đã đóng kết nối MySQL.")
