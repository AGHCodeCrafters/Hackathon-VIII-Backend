from sqlalchemy.orm import Session
from typing import List
from . import models, schemas


def create_task_in_warehouse(db: Session, task: schemas.TaskInWarehouseCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def create_task_from_warehouse(db: Session, task: schemas.TaskFromWarehouseCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks_by_employee_id(db: Session, employee_id: int):
    return db.query(models.Task).filter(models.Task.employee_id == employee_id).all()

