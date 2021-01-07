
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, Column, ForeignKey, Integer, Enum, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProductVariantOptionMap(Base):
    product_variant_id = Column(
        UUID(as_uuid=True), ForeignKey('productvariant.id'))
    product_variant_option_id = Column(UUID(as_uuid=True), ForeignKey(
        'productvarianttypeoption.id'), primary_key=True)
