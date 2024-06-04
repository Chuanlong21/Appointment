# controllers/appointment_controller.py
from models.user import User
from datetime import datetime, timedelta
from services.excel_service import init_excel_file,add_to_excel


def add(user_data) -> {}:
    program = _get_program(user_data.get("program"))
    end_time = _get_end_time(user_data.get("startTime"), program[1])

    new_user = User(**user_data)
    new_user.update_end_time(end_time)
    # init_excel_file()
    # add_to_excel(new_user)
    print(new_user)

    return {
        "id": new_user.id,
        "startTime": new_user.startTime,
        "endTime": new_user.endTime
    }


# 原本program的格式是 Foot,45
# 所以需要把它转换并且返回元组
def _get_program(pro: str) -> []:
    temp = pro.split(',')
    program = temp[0]
    duration = int(temp[1])
    return [program, duration]


# 计算end time
def _get_end_time(start_time: str, duration: int) -> str:
    start = datetime.strptime(start_time, '%H:%M')
    end_datetime = start + timedelta(minutes=duration)
    return end_datetime.strftime('%H:%M')
