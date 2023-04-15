from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...config import database

class Employee(database.Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    tasks = relationship("Task", back_populates="employee")
