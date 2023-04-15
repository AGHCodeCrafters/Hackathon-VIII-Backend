from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


# EMPLOYEE

class EmployeeBase(BaseModel):
    name: str


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeGet(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    products_delivered: Optional[int] = 0
    bezoski: Optional[int] = 0

    class Config:
        orm_mode = True

# # ITEM

# class ItemBase(BaseModel):
#     loction: int


# class ItemCreate(ItemBase):
#     status : str = "on-stock"


# class Item(ItemBase):
#     id: int
#     loction : int
#     status: str = "on-stock"

#     class Config:
#         orm_mode = True


# # TASKS

# class TaskBase(BaseModel):
#     item_id: int
#     employee_id: int
#     destination: int


# class TaskCreate(TaskBase):
#     status : str = "to-pick"
    

# class TaskStatusChange(TaskBase):
#     status : str 
    
    


# class Task(TaskBase):
#     id: int
#     employee_id: int
#     item_id: int
#     status : str

#     class Config:
#         orm_mode = True


# class EmployeeTasks(Employee):
#     tasks: List[Task] = []

#     class Config:
#         orm_mode = True


# class ItemTasks(Item):
#     tasks: List[Task] = []

#     class Config:
#         orm_mode = True