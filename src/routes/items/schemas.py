from pydantic import BaseModel

class ItemBase(BaseModel):
    location: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


