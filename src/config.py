"""
config.py – Cấu hình kết nối Database tập trung
Đọc thông tin từ file .env (không commit .env lên git!)

Hướng dẫn:
  1. Copy file .env.example thành .env
  2. Điền thông tin kết nối SQL Server của bạn vào .env
  3. Chạy ứng dụng bình thường
"""
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env (nằm ở thư mục gốc project)
_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(_base_dir, '.env'))

# Đọc từng tham số, fallback về giá trị mặc định an toàn
DB_DRIVER = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')
DB_SERVER = os.getenv('DB_SERVER', 'localhost')
DB_NAME   = os.getenv('DB_NAME',   'BAN_NUOC')
DB_UID    = os.getenv('DB_UID',    '')
DB_PWD    = os.getenv('DB_PWD',    '')

# Chuỗi kết nối hoàn chỉnh – dùng chung toàn bộ project
CONNECTION_STRING = (
    f"Driver={{{DB_DRIVER}}};"
    f"Server={DB_SERVER};"
    f"Database={DB_NAME};"
    f"UID={DB_UID};"
    f"PWD={DB_PWD};"
)
