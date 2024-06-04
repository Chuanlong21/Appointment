import os
import csv
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
            first_name = row['firstName']
            last_name = row['lastName']
            USER_DATA_CACHE[(first_name, last_name)] = row


def save_user_data():
    global USER_DATA_CACHE
    with open(FILE_PATH, mode='w', newline='') as file:
        fieldnames = ['firstName', 'lastName', 'startTime', 'endTime', 'notes', 'program']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in USER_DATA_CACHE.values():
            writer.writerow(user)
    print("User data saved:", USER_DATA_CACHE)  # Debug output


def set_user_data(first_name, last_name, key, value):
    if not USER_DATA_CACHE:
        load_user_data()
    if (first_name, last_name) in USER_DATA_CACHE:
        USER_DATA_CACHE[(first_name, last_name)][key] = value
    # else:
    #     USER_DATA_CACHE[(first_name, last_name)] = {
    #         'firstName': first_name,
    #         'lastName': last_name,
    #         'startTime': '',
    #         'endTime': '',
    #         'notes': '',
    #         'program': ''
    #     }
    #     USER_DATA_CACHE[(first_name, last_name)][key] = value
    # save_user_data()


def get_user_data(first_name, last_name):
    if not USER_DATA_CACHE:
        load_user_data()
    return USER_DATA_CACHE.get((first_name, last_name))


def get_data_by_name(first_name, last_name, data_name: str):
    user_data = get_user_data(first_name, last_name)
    if not user_data:
        return None
    data_mapping = {
        'startTime': user_data['startTime'],
        'endTime': user_data['endTime'],
        'notes': user_data['notes'],
        'program': user_data['program']
    }
    return data_mapping.get(data_name)
