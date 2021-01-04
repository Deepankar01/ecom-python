from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    title = Column(String, index=True)
    description = Column(String, index=True)
    sellers = relationship('Seller', secondary='prdseller')
    meta = relationship('ProductMeta', secondary='productmeta')
