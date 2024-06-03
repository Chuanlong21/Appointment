from typing import Optional
from pydantic import BaseModel


# 要实现变量私有化，只公开方法！！！
class Event(BaseModel):
    uid: str = ""
    program: str = ""
    startTime: str
    endTime: str
    employee: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self):
        return {
            'uid': self.uid,
            'startTime': self.startTime,
            'endTime': self.endTime
        }
