
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, Column, ForeignKey, Integer, Enum, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProductVariant(Base):
    prd_seller_id = Column(UUID(as_uuid=True), ForeignKey(
        'prdstore.id'))
    sku = Column(String, nullable=False)
    regular_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    max_order_quantity = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False)
    variant_options = relationship(
        'ProductVariantTypeOption', secondary="productvariantoptionmap")
    # find a way to get this
    # variant_type = relationship(
    #     'ProductVariantType', secondary='productvarianttypeoption', uselist=False)
    # product = relationship('Product', secondary='prdstore')
