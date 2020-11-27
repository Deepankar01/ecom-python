from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401
    from .user import User  # noqa: F401


class Cart(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    products = relationship('Product', secondary='CartProducts')
