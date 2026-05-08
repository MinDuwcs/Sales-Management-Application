# ☕ Coffee F5 – Phần Mềm Quản Lý Bán Nước (POS System)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt6-GUI-green?logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL%20Server-Database-red?logo=microsoftsqlserver&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-Analytics-orange" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
</p>

> **Ứng dụng quản lý bán hàng (POS – Point of Sale)** dành cho quán cà phê / nước giải khát, xây dựng bằng Python và PyQt6 với giao diện desktop đầy đủ tính năng.

---

## 📋 Mục lục

- [Tính năng](#-tính-năng)
- [Tech Stack](#-tech-stack)
- [Cấu trúc project](#-cấu-trúc-project)
- [Cài đặt & Chạy](#-cài-đặt--chạy)
- [Database Schema](#-database-schema)
- [Tác giả](#-tác-giả)

---

## ✨ Tính năng

### 🔐 Quản lý tài khoản
- Đăng nhập / Đăng ký tài khoản nhân viên
- Xác thực người dùng theo ID nhân sự
- Quên mật khẩu / Đặt lại mật khẩu

### 🧾 Màn hình POS bán hàng
- Hiển thị menu đồ uống dạng lưới, hỗ trợ tìm kiếm & gợi ý tự động
- Tạo đơn hàng theo bàn (10 bàn), chuyển bàn linh hoạt
- Thêm / xóa / điều chỉnh số lượng món trong đơn
- Tính tổng tiền tự động, hiển thị hóa đơn

### 💳 Thanh toán
- Hỗ trợ nhiều hình thức: Tiền mặt, Chuyển khoản
- Tạo mã **QR Code** thanh toán tự động
- In hóa đơn

### 🍹 Quản lý Menu
- Thêm / Xóa / Xem danh sách món
- Phân loại món, giá tiền, mô tả
- Hỗ trợ ảnh món ăn

### 📦 Quản lý Nguyên Liệu & Tồn Kho
- Thêm / Xóa nguyên liệu
- Cập nhật số lượng tồn kho (nhập / xuất)
- Tìm kiếm nguyên liệu theo tên
- Theo dõi ngày cập nhật

### 📊 Thống kê Doanh Thu
- Xem tổng doanh thu toàn thời gian
- Lọc theo tháng / năm
- Tính doanh thu trung bình
- Biểu đồ trực quan bằng Matplotlib & Seaborn

### 👥 Quản lý Nhân Viên
- Xem danh sách nhân viên
- Quản lý thông tin nhân sự

---

## 🛠 Tech Stack

| Thành phần | Công nghệ |
|-----------|-----------|
| Ngôn ngữ | Python 3.10+ |
| GUI Framework | PyQt6 |
| Database | Microsoft SQL Server (pyodbc) |
| Data Visualization | Matplotlib, Seaborn |
| QR Code | qrcode |
| Image Processing | Pillow (PIL) |
| Database Design | draw.io (ERD) |

---

## 📁 Cấu trúc project

```
coffee-f5-pos/
├── src/
│   ├── app.py                  # Entry point – Màn hình chính POS & Login
│   ├── config.py               # Cấu hình kết nối DB (đọc từ .env)
│   ├── Mon.py                  # Module quản lý menu món
│   ├── NguyenLieuTonKho.py     # Module quản lý nguyên liệu tồn kho
│   ├── doanh_thu.py            # Module thống kê doanh thu
│   └── testing.py              # SQLite-based testing utilities
├── data/
│   └── menu_mon_an.csv         # Dữ liệu menu mẫu
├── docs/
│   └── Phan_Mem_Ban_Nuoc.drawio  # Sơ đồ ERD database
├── .env.example                # Template cấu hình kết nối DB
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Cài đặt & Chạy

### Yêu cầu hệ thống
- Python 3.10+
- Microsoft SQL Server (local hoặc remote)
- ODBC Driver 17 for SQL Server

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/coffee-f5-pos.git
cd coffee-f5-pos
```

### 2. Tạo môi trường ảo & cài dependencies

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Cấu hình kết nối Database

```bash
cp .env.example .env
```

Mở file `.env` và điền thông tin kết nối SQL Server của bạn:

```
DB_SERVER=your_server_name
DB_NAME=BAN_NUOC
DB_UID=your_username
DB_PWD=your_password
```

> **Lưu ý:** Cần tạo database `BAN_NUOC` trên SQL Server trước.  
> Sơ đồ ERD xem tại `docs/Phan_Mem_Ban_Nuoc.drawio`.

### 4. Chạy ứng dụng

```bash
python src/app.py
```

---

## 🗄 Database Schema

Sơ đồ ERD đầy đủ tại [`docs/Phan_Mem_Ban_Nuoc.drawio`](docs/Phan_Mem_Ban_Nuoc.drawio)

**Các bảng chính:**

| Bảng | Mô tả |
|------|-------|
| `ACCOUNT` | Tài khoản người dùng |
| `NHAN_SU` | Thông tin nhân viên |
| `MON` | Danh sách món ăn / đồ uống |
| `HOA_DON` | Hóa đơn thanh toán |
| `NGUYENLIEU_TONKHO` | Nguyên liệu & tồn kho |

---

## 🎯 Kỹ năng thể hiện qua project

- ✅ **OOP** – Thiết kế hướng đối tượng: `UserManager`, `LoginWindow`, `CoffeePOS`, ...
- ✅ **GUI Desktop** – Xây dựng giao diện hoàn chỉnh với PyQt6 (layouts, dialogs, tables)
- ✅ **Database** – Kết nối & truy vấn SQL Server qua pyodbc; thiết kế schema với ERD
- ✅ **Data Analysis** – Thống kê và trực quan hoá doanh thu bằng Matplotlib/Seaborn
- ✅ **API Integration** – Tạo QR Code thanh toán động
- ✅ **Security** – Tách credentials ra khỏi source code, dùng biến môi trường
- ✅ **Modular Architecture** – Tách module rõ ràng (config, Mon, NguyenLieu, DoanhThu)
- ✅ **Error Handling** – Validate dữ liệu đầu vào, xử lý lỗi kết nối DB

---

## 👤 Tác giả

**[Tên của bạn]**  
📧 [email@example.com]  
🔗 [LinkedIn Profile]  
🐙 [GitHub Profile]

---

<p align="center">Made with ❤️ using Python & PyQt6</p>
