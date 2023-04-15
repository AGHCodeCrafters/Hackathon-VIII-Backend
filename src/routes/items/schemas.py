from pydantic import BaseModel

class ItemBase(BaseModel):
    location: str
    code : int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


