from typing import List
from pydantic import UUID4
from fastapi import APIRouter, HTTPException
from app.schemas import Product as ProductSchema
from app.models import Product
from app.db.database import database

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
async def read_items():
    query = Product.__table__.select()
    return await database.fetch_all(query)


@router.get("/{product_id}", response_model=ProductSchema)
async def read_items(product_id: UUID4):
    query = Product.__table__.select().where(Product.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
