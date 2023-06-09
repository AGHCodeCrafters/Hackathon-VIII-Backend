from pydantic import BaseModel
from ..items import models
from sqlalchemy.orm import Session


class TaskBase(BaseModel):
    item_id: int
    employee_id: int

    destination_location: str
    type: str
    bezoski_value: int

class TaskCreate(TaskBase):
    status = "IN_PROGRESS"


class Task(TaskBase):
    id: int
    status: str

    class Config:
        orm_mode = True
