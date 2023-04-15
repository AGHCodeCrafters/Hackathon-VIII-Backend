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

@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskBase, db: Session = Depends(get_db)):
    db_task = crud.create_task(db=db, task=task)
    return db_task

# READ
@router.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    return tasks


