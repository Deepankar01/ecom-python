from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    category_id = Column(UUID(as_uuid=True), ForeignKey('category.id'))
    title = Column(String, index=True)
    description = Column(String, index=True)
    info = relationship('PrdStore', backref='product')
    price = relationship('ProductPrice', secondary='prdstore')
    store = relationship('Store', secondary='prdstore')
    meta = relationship('ProductMeta', backref="prd")
    category = relationship('Category', backref="product")
