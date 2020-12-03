from hashlib import sha256
from sqlalchemy import Boolean, Column, String
from app.db.base_class import Base


class User(Base):
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean(), default=False)

    def check_password(self, hashed_password, plain_password) -> bool:
        password, salt = hashed_password.split(':')
        return password == sha256(salt.encode() + plain_password.encode()).hexdigest()
