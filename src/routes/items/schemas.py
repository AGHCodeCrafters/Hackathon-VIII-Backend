from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    code: int
    current_location: str
    status: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    code: Optional[int] = None


class ItemInDBBase(ItemBase):
    id: int
    code: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemGet(ItemInDBBase):
    status: Optional[str] = None

class ItemStatusUpdate(BaseModel):
    status: str
