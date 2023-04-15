from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database

from ...routes.employees.models import *
from ...routes.items.models import *



class Task(database.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    item_code = Column(Integer, index=True)
    
    pickup = Column(String(255), index=True) 
    destination = Column(String(255), index=True)
    
    employee_name = Column(String(255), index=True)
    
    status = Column(String(255), nullable=False, default="to-pick") # PENDING - IN PROGRESS - COMPLETE
