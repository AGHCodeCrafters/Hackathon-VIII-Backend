from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    aisle: Optional[int] = None
    shelf: Optional[int] = None
    status: str


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

