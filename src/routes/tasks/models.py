from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ...config import database


class Employee(database.Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)

    products_delivered = Column(Integer, index=True, default=0)
    bezoski = Column(Integer, index=True, default=0)

# class Tasks(database.Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True, index=True)
#     employee_id = Column(Integer, ForeignKey("employees.id"))

#     destination = Column(Integer, index=True)
#     item_id = Column(Integer, ForeignKey("items.id"))
#     status = Column(String(255), nullable=False, default="to-pick") # to-pick - In-Progress - finished
    

#     #dodajemy później czas

#     employee = relationship("Employee", back_populates="transactions")
#     item = relationship("Item", back_populates="transactions")


# class Item(database.Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     loction = Column(Integer, index=True)
#     status = Column(String(255), nullable=False, default="on-shelf") # Na półce - na wózku - na tirze
