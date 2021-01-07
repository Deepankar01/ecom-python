
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, Column, ForeignKey, Integer, Enum, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProductVariantTypeOption(Base):
    variant_type_id = Column(UUID(as_uuid=True), ForeignKey(
        'productvarianttype.id'))
    option = Column(String, nullable=False)
