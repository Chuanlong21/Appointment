from pydantic import BaseModel, Field
from typing import List, Optional
from utils.encode import generate_user_id
from models.event import Event


# 要实现变量私有化，只公开方法！！！
class User(BaseModel):
    firstName: str
    lastName: str
    email: str = ""
    phone: str = ""
    id: str = Field(default_factory=generate_user_id)
    events: List[Event] = []

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self):
        return self.dict()



    def add_event(self, event: Event):
        self.events.append(event)
