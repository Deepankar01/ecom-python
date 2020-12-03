from typing import Optional

from pydantic import BaseModel, UUID4


class SellerBase(BaseModel):
    title: str
    description: Optional[str] = None


class SellerCreate(SellerBase):
    pass


class Seller(SellerBase):
    id: UUID4

    class Config:
        orm_mode = True
