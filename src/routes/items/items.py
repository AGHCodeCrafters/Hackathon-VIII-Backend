from fastapi import HTTPException, APIRouter, Depends, status
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



@router.post("/items", status_code=status.HTTP_201_CREATED)
def create_items(items: List[schemas.ItemCreate], db: Session = Depends(get_db)):
    for item in items:
        db_item = db.query(models.Item).filter(models.Item.code == item.code).first()
        if db_item:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item with this code already exists")
        db_item = models.Item(**item.dict())
        db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"msg": "Items created successfully"}


@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items



# Cmentarzysko kodu

# @router.post("/items/", response_model=schemas.Item)
# def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_item(db=db, item=item)
