from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
router = APIRouter()


class StructureRsp(BaseModel):
    data: dict
    success: str

    class Config:
        arbitrary_types_allowed = True


@router.get("/{client_id}/{phase_id}", response_model=StructureRsp)
async def read_structures(phase_id: int, client_id: int):
    return {"data": {}, "success": True}
