from pydantic import BaseModel
from ..items import models
from sqlalchemy.orm import Session


class TaskBase(BaseModel):
    item_id: int
    employee_id: int
    origin_location: str
    destination_location: str

class TaskCreate(TaskBase):
    pass


    
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
