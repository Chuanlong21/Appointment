import os
import pandas as pd
from openpyxl import load_workbook

from models.user import User

DATA_DIR = 'data'
FILE_NAME = 'info.xlsx'
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)


def init_excel_file():
    """初始化Excel文件，添加标题"""
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=[
            "uid",
            "firstName",
            "lastName",
            "email",
            "phone",
            "program",
            "startTime",
            "endTime",
            "employee",
            "notes"
        ])
        df.to_excel(FILE_PATH, index=False)


def add_to_excel(user: User):
    """添加联系人信息到Excel文件"""
    new_data = {
        "uid": [user.id],
        "firstName": [user.firstName],
        "lastName": [user.lastName],
        "email": [user.email],
        "phone": [user.phone],
        "program": [user.program],
        "startTime": [user.startTime],
        "endTime": [user.endTime],
        "employee": [user.employee],
        "notes": [user.notes]
    }

    new_df = pd.DataFrame(new_data)
    book = load_workbook(FILE_PATH)
    with pd.ExcelWriter(FILE_PATH, engine='openpyxl') as writer:
        writer.book = book
        existing_df = pd.read_excel(FILE_PATH)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        updated_df.to_excel(writer, index=False)
