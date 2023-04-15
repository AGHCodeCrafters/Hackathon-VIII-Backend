from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from ...config import database  # import SessionLocal, engine

database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(tags=["Items"])


def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_code(db, item_code=item.code)
    if db_item:
        raise HTTPException(status_code=400, detail="Item code already registered")
    return crud.create_item(db=db, item=item)

@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.delete_item(db=db, item_id=item_id)

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/code/{item_code}", response_model=schemas.Item)
def read_item_by_code(item_code: int, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_code(db, item_code=item_code)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
