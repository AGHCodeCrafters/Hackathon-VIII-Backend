from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    item_code: int
    pickup: str
    destination: str
    employee_name: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    status: Optional[str]

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    status: str

    class Config:
        orm_mode = True
