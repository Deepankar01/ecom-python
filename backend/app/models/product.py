from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Product(Base):
    title = Column(String, index=True)
    description = Column(String, index=True)
    sellers = relationship('Seller', secondary='PrdSeller')
    meta = relationship('Meta', secondary='ProductMeta')
