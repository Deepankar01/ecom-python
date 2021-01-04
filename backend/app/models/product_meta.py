from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base


class ProductMeta(Base):
    product_id = Column(UUID(as_uuid=True), ForeignKey(
        'product.id'), primary_key=True)
    name = Column(String, index=True)
    value = Column(String, index=True)
