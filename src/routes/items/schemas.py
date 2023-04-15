from pydantic import BaseModel
from typing import List


class ItemBase(BaseModel):
    location: str
    code : int

class ItemCreate(ItemBase):
    pass

class ItemListCreate(BaseModel):
    items: List[ItemCreate]


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemList(ItemBase):
    items: List[Item] 


