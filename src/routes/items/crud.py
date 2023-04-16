from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException

from . import models, schemas


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    try:
        db.commit()
        db.refresh(db_item)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Item with this code already exists")
    return db_item



def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).order_by(models.Item.id).offset(skip).limit(limit).all()
