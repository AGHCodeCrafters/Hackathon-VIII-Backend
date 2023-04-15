from typing import List
from sqlalchemy.orm import Session

from . import models, schemas


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def update_task_status(db: Session, task_id: int, status: str):
    db.query(models.Task).filter(models.Task.id == task_id).update({"status": status})
    db.commit()
    return {"message": "Task status updated successfully."}


def delete_task(db: Session, task_id: int):
    db.query(models.Task).filter(models.Task.id == task_id).delete()
    db.commit()
    return {"message": "Task deleted successfully."}


def get_tasks_by_status(db: Session, status: str, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.status == status).offset(skip).limit(limit).all()
