from typing import List
from pydantic import UUID4
from fastapi import APIRouter, HTTPException
from app.schemas import Seller as SellerSchema
from app.models import Seller
from app.db.database import database
router = APIRouter()


@router.get("/", response_model=List[SellerSchema])
async def read_items():
    query = Seller.__table__.select()
    return await database.fetch_all(query)


@router.get("/{seller_id}", response_model=SellerSchema)
async def read_item(product_id: UUID4):
    query = Seller.__table__.select().where(Seller.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Seller not found")
    return product
