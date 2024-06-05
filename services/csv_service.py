import os
import csv
import shutil
import tempfile

from models.user import User

DATA_DIR = 'data'
FILE_NAME = 'info.csv'
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)
USER_DATA_CACHE = {}


def init_csv_file():
    """初始化 CSV 文件"""
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["uid", "firstName", "lastName", "email", "phone", "program", "startTime", "endTime", "employee",
                 "notes"])


def add_to_csv(user: User):
    """将用户数据添加到 CSV 文件"""
    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            user.id, user.firstName, user.lastName, user.email, user.phone,
            user.program, user.startTime, user.endTime, user.employee, user.notes
        ])


def load_user_data():
    global USER_DATA_CACHE
    if not os.path.exists(FILE_PATH):
        return None
    with open(FILE_PATH, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            phone = row['phone']
            USER_DATA_CACHE[phone] = row


def save_user_data():
    global USER_DATA_CACHE
    temp_file = tempfile.NamedTemporaryFile(mode='w', newline='', delete=False)
    with open(FILE_PATH, mode='r', newline='') as file, temp_file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            key = (row['phone'])
            if key in USER_DATA_CACHE:
                row.update(USER_DATA_CACHE[key])
            writer.writerow(row)
    shutil.move(temp_file.name, FILE_PATH)
    print("User data saved:", USER_DATA_CACHE)  # Debug output


def set_user_data(phone, key, value):
    if not USER_DATA_CACHE:
        load_user_data()
    if phone in USER_DATA_CACHE:
        USER_DATA_CACHE[phone][key] = value
    else:
        USER_DATA_CACHE[phone] = {
            'firstName': '',
            'lastName': '',
            'phone': phone,
            'startTime': '',
            'endTime': '',
            'notes': '',
            'program': ''
        }
        USER_DATA_CACHE[phone][key] = value
    save_user_data()


def get_user_data(phone):
    if not USER_DATA_CACHE:
        load_user_data()
    return USER_DATA_CACHE.get(phone)


def get_data_by_name(phone, data_name: str):
    user_data = get_user_data(phone)
    if not user_data:
        return None
    data_mapping = {
        'startTime': user_data['startTime'],
        'endTime': user_data['endTime'],
        'notes': user_data['notes'],
        'program': user_data['program']
    }
    return data_mapping.get(data_name)
