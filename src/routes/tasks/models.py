from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database
from ..items.models import Item


class Task(database.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    origin_location = Column(String)
    destination_location = Column(String)

    employee = relationship("Employee", back_populates="tasks")
    item = relationship("Item", back_populates="tasks")