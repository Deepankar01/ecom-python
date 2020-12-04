from typing import List
from pydantic import UUID4
from fastapi import APIRouter, HTTPException
from app.schemas import User as UserSchema, UserCreate, CreateUser
from app.models import User
from app.db.database import database
from asyncpg.exceptions import UniqueViolationError
router = APIRouter()


@router.get("/", response_model=List[UserSchema])
async def get_list():
    query = User.__table__.select()
    return await database.fetch_all(query)


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: UUID4):
    query = User.__table__.select().where(User.id == user_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="User not found")
    return product


@router.post("/", response_model=CreateUser)
async def create_user(user: UserCreate):
    '''
        Use firebase authetication for user authentication and creation and seller signup as well
    '''
    query = User.__table__.insert().values(email=user.email, id=user.id_hash, hashed_password=user.hash_password,
                                           is_active=True, is_superuser=False)
    try:
        await database.execute(query)
        return {"id": user.id_hash, "email": user.email}
    except UniqueViolationError:
        raise HTTPException(status_code=401, detail="User already exists")
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
