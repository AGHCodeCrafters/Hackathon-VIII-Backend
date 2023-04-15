from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database

from ...routes.employees.models import *
from ...routes.items.models import *



class Task(database.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    item_id = Column(Integer, ForeignKey("items.id"))
    destination_gate = Column(Integer, index=True, nullable=True)

    task_type = Column(String(255), nullable=False, index=True) # IN - OUT
    pick_gate = Column(Integer, index=True, nullable=True)

    destination_alias = Column(String(255))
    destination_shelf = Column(String(255))

    status = Column(String(255), nullable=False, default="to-pick")

    employees = relationship("Employee", back_populates="tasks")
    items = relationship("Item", back_populates="tasks")
