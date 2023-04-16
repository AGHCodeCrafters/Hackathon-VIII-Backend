from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database

class Item(database.Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), unique=True)
    location = Column(String(255))
    
    tasks = relationship("Task", back_populates="item")
