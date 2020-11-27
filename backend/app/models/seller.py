from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401


class Seller(Base):
    id = Column(Integer, primary_key=True, index=True)
    products = relationship('Product', secondary='PrdSeller')
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))
