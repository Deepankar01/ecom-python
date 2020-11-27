from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, Float, String
from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product


class ProductMeta(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    name = Column(String, index=True)
    value = Column(String, index=True)
