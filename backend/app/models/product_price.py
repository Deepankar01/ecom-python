from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProductPrice(Base):
    actual_price = Column(Float)
    discounted_price = Column(Float)
    shipping_charges = Column(Float)
