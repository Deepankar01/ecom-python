from typing import Optional

from pydantic import BaseModel, UUID4


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: UUID4
    title: str

    class Config:
        orm_mode = True
