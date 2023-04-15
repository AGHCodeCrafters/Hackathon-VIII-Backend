from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    location: Optional[int] = None
    status: str


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

