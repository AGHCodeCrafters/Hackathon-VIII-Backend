from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from ...config import database  # import SessionLocal, engine

database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(tags=["Employees"])

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.create_employee(db, employee)
    return db_employee

@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

