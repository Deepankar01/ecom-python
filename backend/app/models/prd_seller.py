from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class PrdStore(Base):
    store_id = Column(UUID(as_uuid=True), ForeignKey(
        'store.id'), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey(
        'product.id'), primary_key=True)
    is_active = Column(Boolean, default=False)
    price_id = Column(UUID(as_uuid=True), ForeignKey(
        'productprice.id'), primary_key=True)
    coupon = relationship('ProductCoupon', backref="prdstore")
