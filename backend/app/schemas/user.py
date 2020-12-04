from uuid import uuid4
from hashlib import sha256
from typing import List
from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

    @property
    def id_hash(self):
        return uuid4().hex

    @property
    def hash_password(self):
        salt = uuid4().hex
        return sha256(salt.encode() + self.password.encode()).hexdigest() + ':' + salt


class CreateUser(UserBase):
    id: UUID4


class User(UserBase):
    id: UUID4
    is_active: bool

    class Config:
        orm_mode = True
