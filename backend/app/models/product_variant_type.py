
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, Column, ForeignKey, Integer, Enum, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProductVariantType(Base):
    name = Column(String, nullable=False)
