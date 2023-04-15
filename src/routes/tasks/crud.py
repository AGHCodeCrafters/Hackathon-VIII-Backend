from sqlalchemy.orm import Session
from typing import List
from . import models, schemas


def create_employee(db: Session, post: schemas.EmployeeCreate):
    db_empl = models.Employee(**post.dict())
    db.add(db_empl)
    db.commit()
    db.refresh(db_empl)
    return db_empl

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()



# def create_task(db: Session, post: schemas.TaskCreate):
#     db_task = models.Tasks(**post.dict())
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     return db_task

# def create_task(db: Session, post: schemas.ItemCreate):
#     db_item = models.Tasks(**post.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item