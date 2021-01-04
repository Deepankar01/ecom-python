from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Cart(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    products = relationship('Product', secondary='cartproduct')
