from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
from app.db.base_class import Base


class CartProduct(Base):
    cart_id = Column(UUID(as_uuid=True), ForeignKey(
        'cart.id'), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey(
        'product.id'), primary_key=True)
