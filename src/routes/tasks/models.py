from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database
from ..items.models import Item
from ..employees.models import Employee


from enum import Enum


class Task(database.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    destination_location = Column(String(255))
    type = Column(String(255))
    status = Column(String(255), default="IN_PROGRESS")
    bezoski_value = Column(Integer, default=1)


    employee = relationship("Employee", back_populates="tasks")
    item = relationship("Item", back_populates="tasks")