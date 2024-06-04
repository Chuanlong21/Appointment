import os
import csv
from models.user import User

DATA_DIR = 'data'
FILE_NAME = 'info.csv'
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)


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



