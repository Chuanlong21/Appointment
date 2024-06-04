from pydantic import BaseModel, Field
from typing import Optional
from utils.encode import generate_user_id


# 要实现变量私有化，只公开方法！！！
class User(BaseModel):
    firstName: str
    lastName: str
    email: str = ""
    phone: str = ""
    program: str = ""
    startTime: str = ""
    endTime: str = ""
    employee: Optional[str] = None
    notes: Optional[str] = None
    id: str = Field(default_factory=generate_user_id)

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self):
        return self.dict()

    def update_start_time(self, start_time: str):
        self.startTime = start_time

    def update_end_time(self, end_time: str):
        self.endTime = end_time
