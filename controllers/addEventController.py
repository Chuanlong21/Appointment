# controllers/appointment_controller.py
from models.user import User
from datetime import datetime, timedelta
from services.csv_service import init_csv_file, add_to_csv, get_data_by_name, set_user_data


def add(user_data) -> {}:
    program = _get_program(user_data.get("program"))
    end_time = _get_end_time(user_data.get("startTime"), program[1])
    new_user = User(**user_data)
    new_user.update_end_time(end_time)
    new_user.update_program(program[0])

    if get_data_by_name(user_data.get("phone"), "program") is None:
        init_csv_file()
        add_to_csv(new_user)
    else:
        set_user_data(new_user.phone, "email", new_user.email)
        set_user_data(new_user.phone, "program", new_user.program)
        set_user_data(new_user.phone, "startTime", new_user.startTime)
        set_user_data(new_user.phone, "endTime", new_user.endTime)
        set_user_data(new_user.phone, "employee", new_user.employee)

    return {
        "firstName": new_user.firstName,
        "lastName": new_user.lastName,
        "startTime": new_user.startTime,
        "endTime": new_user.endTime
    }


def get_events():
    return


# 原本program的格式是 Foot,45
# 所以需要把它转换并且返回元组
def _get_program(pro: str) -> []:
    temp = pro.split(',')
    program = temp[0]
    duration = int(temp[1])
    return [program, duration]


# 计算end time
def _get_end_time(start_time: str, duration: int) -> str:
    print(start_time)
    start = datetime.strptime(start_time, '%H:%M')
    end_datetime = start + timedelta(minutes=duration)
    return end_datetime.strftime('%H:%M')
