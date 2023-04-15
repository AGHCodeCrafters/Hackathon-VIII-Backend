from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

from typing import List

def create_task(db: Session, task: schemas.TaskBase):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_tasks_by_employee_id(db: Session, employee_id: int) -> List[models.Task]:
    tasks = db.query(models.Task).filter(models.Task.employee_id == employee_id).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks


def complete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.status != "COMPLETED").first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_item = db.query(models.Item).filter(models.Item.id == db_task.item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_employee = db.query(models.Employee).filter(models.Employee.id == db_task.employee_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Employee not found")

    db_employee.bezoski += 1
    db_item.location = db_task.destination_location
    db_task.status = "COMPLETED"
    db.commit()
    return {"message": "Task completed successfully"}


