from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean
from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401
    from .seller import Seller  # noqa: F401


class PrdSeller(Base):
    seller_id = Column(UUID(as_uuid=True), ForeignKey('seller.id'), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey('product.id'), primary_key=True)
    is_active = Column(Boolean, default=False)
    price = Column(Float)
