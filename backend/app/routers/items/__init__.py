from typing import List
from fastapi import APIRouter
from app.schemas import Item as ItemSchema
from app.models import Item
from app.db.database import database

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
async def read_items():
    query = Item.__table__.select()
    return await database.fetch_all(query)
