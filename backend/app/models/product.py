from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    title = Column(String, index=True)
    description = Column(String, index=True)
    info = relationship('PrdStore', backref='product')
    price = relationship('ProductPrice', secondary='prdstore')
    store = relationship('Store', secondary='prdstore')
    meta = relationship('ProductMeta', backref="prd")
