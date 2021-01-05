from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    title = Column(String, index=True)
    description = Column(String, index=True)
    info = relationship('PrdSeller', backref='product')
    price = relationship('ProductPrice', secondary='prdseller')
    sellers = relationship('Seller', secondary='prdseller')
    meta = relationship('ProductMeta', backref="prd")
