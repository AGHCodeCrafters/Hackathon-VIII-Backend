from typing import List, Optional
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
