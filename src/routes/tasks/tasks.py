from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from ...config import database  # import SessionLocal, engine

database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(tags=["Tasks"])


def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/tasks/IN", response_model=schemas.TaskInWarehouseCreate)
def create_task_in_warehouse(task: schemas.TaskInWarehouseCreate, db: Session = Depends(get_db)):
    return crud.create_task_in_warehouse(db=db, task=task)


@router.post("/tasks/OUT", response_model=schemas.TaskFromWarehouseCreate)
def create_task_from_warehouse(task: schemas.TaskFromWarehouseCreate, db: Session = Depends(get_db)):
    return crud.create_task_from_warehouse(db=db, task=task)

@router.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/tasks/employee/{employee_id}", response_model=list[schemas.Task])
def read_tasks_by_employee_id(employee_id: int, db: Session = Depends(get_db)):
    db_tasks = crud.get_tasks_by_employee_id(db, employee_id=employee_id)
    if not db_tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return db_tasks


