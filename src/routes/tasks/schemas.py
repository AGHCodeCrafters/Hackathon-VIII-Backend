from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class TaskBase(BaseModel):
    employee_id: int
    item_id: int
    task_type: str
    status: str


class TaskCreate(TaskBase):
    pass


class TaskInWarehouseCreate(TaskBase):
    task_type: str = "IN"
    pick_gate : int
    destination_aisle: int
    destination_shelf: int


class TaskFromWarehouseCreate(TaskBase):
    task_type: str = "OUT"
    destination_gate : int

class Task(TaskBase):
    id: int
    destination_gate : Optional[int] = None
    pick_gate : Optional[int] = None
    destination_alias: Optional[str] = None
    destination_shelf: Optional[str] = None

    class Config:
        orm_mode = True
