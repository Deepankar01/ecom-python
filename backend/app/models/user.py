from sqlalchemy import Boolean, Column, String
from app.db.base_class import Base


class User(Base):
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean(), default=False)
