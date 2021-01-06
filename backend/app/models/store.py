from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Store(Base):
    buisness_name = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    seller_id = Column(UUID(as_uuid=True), ForeignKey("seller.id"))
    is_store_pickup = Column(Boolean, nullable=False)
    is_same_home_delivery = Column(Boolean, nullable=False)
    extra_delivery_charge = Column(Float, default=0)
    minimum_order_amount = Column(Float, default=0)
    is_shipping = Column(Boolean, nullable=False)
    address_id = Column(UUID(as_uuid=True), ForeignKey("address.id"))
    address = relationship('Address', backref="store", uselist=False)
    store_manager = relationship(
        'StoreManager', backref="store", uselist=False)
    # maximum_distance
    # images
    # logo
    # documents
