from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey
from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401
    from .user import User  # noqa: F401


class CartProduct(Base):
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('cart.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
