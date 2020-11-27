from typing import List
from pydantic import BaseModel
from .product import Product


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Product] = []

    class Config:
        orm_mode = True
