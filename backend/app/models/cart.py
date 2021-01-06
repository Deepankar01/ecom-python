from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Cart(Base):
    buyer_id = Column(UUID(as_uuid=True), ForeignKey("buyer.id"))
    products = relationship('Product', secondary='cartproduct')
    buyer = relationship('User', secondary='buyer', uselist=False)
