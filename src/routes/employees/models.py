from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...config import database

class Employee(database.Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    
    bezoski = Column(Integer, default=0)

    tasks = relationship("Task", back_populates="employee")
