import random  # Import để làm việc với số ngẫu nhiên trong Python

import string  # Import để làm việc với các phương thức xử lý chuỗi và bảng mã ký tự trong Python

import os  # Import để tương tác với hệ điều hành và thực hiện các thao tác hệ thống trong Python

# Tạo một chuỗi ngẫu nhiên có độ dài tối thiểu 4 ký tự
def generate_order_id(length=4):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Tạo một chuỗi số ngẫu nhiên có độ dài tối thiểu 4 ký tự
def generate_numeric_order_id(length=4):
    characters = string.digits  # Sử dụng chỉ chữ số
    return ''.join(random.choice(characters) for _ in range(length))

# Tạo một chuỗi ngẫu nhiên có độ dài tối thiểu 12 ký tự
def generate_random_filename(instance, filename, upload_folder):
    ext = filename.split('.')[-1]
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    new_filename = f"{instance.pk}_{random_chars}.{ext}"
    return os.path.join(upload_folder, new_filename)