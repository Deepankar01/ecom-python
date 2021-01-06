import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, Column, ForeignKey, Integer, Enum, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class CouponType(enum.Enum):
    price = 1
    quantity = 2


class ProductCoupon(Base):
    prd_seller_id = Column(UUID(as_uuid=True), ForeignKey(
        'prdstore.id'), primary_key=True)
    coupon_code = Column(String, unique=True)
    expiry_time = Column(DateTime(timezone=True),)
    start_time = Column(DateTime(timezone=True),)
    discount_type = Column(Enum(CouponType), default=CouponType.price)
    is_active = Column(Boolean, default=False)
    count = Column(Integer, default=0)
    product = relationship('Product', secondary='prdstore')
    store = relationship('Store', secondary='prdstore')
