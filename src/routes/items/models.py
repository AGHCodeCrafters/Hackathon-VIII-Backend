from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database



class Item(database.Base):
    __tablename__ = "items"

    id  = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True, index=True)
    current_location = Column(String(255), nullable=False) # 'in: 1; war: 1,1; out: 2'  
    status = Column(String(255), default="GATE-IN") # Na półce - na wózku - na tirze 
