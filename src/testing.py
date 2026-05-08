import sqlite3
import shutil
import os

class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'conn'):
            self.conn.commit()
            self.conn.close()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        ''')

    # --- Lưu trữ Sản Phẩm ---
    def luu_tru_san_pham(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))

    def get_product_by_id(self, product_id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        return self.cursor.fetchone()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def update_product(self, product_id, name, price):
        self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, product_id))

    def delete_product(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    # --- Lưu trữ Đơn Hàng ---
    def luu_tru_don_hang(self, product_id, quantity, total_price):
        self.cursor.execute('INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)',
                            (product_id, quantity, total_price))

    def get_order_by_id(self, order_id):
        self.cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        return self.cursor.fetchone()

    def get_all_orders(self):
        self.cursor.execute('SELECT * FROM orders')
        return self.cursor.fetchall()

    def update_order(self, order_id, product_id, quantity, total_price):
        self.cursor.execute('''
            UPDATE orders
            SET product_id = ?, quantity = ?, total_price = ?
            WHERE id = ?
        ''', (product_id, quantity, total_price, order_id))

    def delete_order(self, order_id):
        self.cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))

    # --- Backup Database ---
    def backup_database(self, backup_file="backup_app.db"):
        if os.path.exists(self.db_name):
            shutil.copy2(self.db_name, backup_file)
            return True
        return False

if __name__ == "__main__":
    with Database() as db:
        db.create_tables()

        while True:
            print("\n==== Menu Đồ Uống ====")
            print("1. Lưu Trữ Danh Sách Đồ Uống Mặc Định")
            print("2. Xem Danh Sách Đồ Uống Đã Lưu")
            print("3. Tạo Đơn Hàng")
            print("4. Xem Danh Sách Đơn Hàng")
            print("5. Backup File Database")
            print("0. Thoát")

            choice = input("Chọn chức năng: ")

            if choice == "1":
                drinks = [
                    ("Trà Sữa", 30000),
                    ("Cà Phê Sữa", 25000),
                    ("Sinh Tố Bơ", 40000),
                    ("Trà Đào", 35000)
                ]
                for name, price in drinks:
                    db.luu_tru_san_pham(name, price)
                print("Đã lưu trữ danh sách đồ uống mặc định.")
            elif choice == "2":
                products = db.get_all_products()
                print("\nDanh Sách Đồ Uống:")
                for p in products:
                    print(f"ID: {p[0]}, Tên: {p[1]}, Giá: {p[2]} VND")
            elif choice == "3":
                product_id = int(input("Nhập ID đồ uống: "))
                quantity = int(input("Nhập số lượng: "))
                product = db.get_product_by_id(product_id)
                if product:
                    total = product[2] * quantity
                    db.luu_tru_don_hang(product_id, quantity, total)
                    print(f"Đã tạo đơn hàng: {product[1]} x {quantity} = {total} VND")
                else:
                    print("Không tìm thấy đồ uống.")
            elif choice == "4":
                orders = db.get_all_orders()
                print("\nDanh Sách Đơn Hàng:")
                for o in orders:
                    print(f"ID: {o[0]}, ID Sản Phẩm: {o[1]}, Số Lượng: {o[2]}, Tổng Giá: {o[3]} VND")
            elif choice == "5":
                if db.backup_database():
                    print("Đã sao lưu file database thành công.")
                else:
                    print("Không tìm thấy file database để sao lưu.")
            elif choice == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")