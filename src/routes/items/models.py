from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database



class Item(database.Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(Integer, index=True)
    status = Column(String(255), default="on-shelf") # Na półce - na wózku - na tirze