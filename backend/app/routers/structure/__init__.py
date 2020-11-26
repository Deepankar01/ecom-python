from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class StructureRsp(BaseModel):
    data: dict
    success: str

    class Config:
        arbitrary_types_allowed = True


@router.get("/{client_id}/{phase_id}", response_model=StructureRsp)
async def read_structures(phase_id: int, client_id: int):
    # database.
    return {"data": {}, "success": True}
