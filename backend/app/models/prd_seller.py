from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from .product import Product
from .seller import Seller

# if TYPE_CHECKING:
#     # noqa: F401
#     # noqa: F401


class PrdSeller(Base):
    seller_id = Column(UUID(as_uuid=True), ForeignKey(
        'seller.id'), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey(
        'product.id'), primary_key=True)
    is_active = Column(Boolean, default=False)
    price = Column(Float)
    sellers = relationship(Seller)
    product = relationship(Product)
