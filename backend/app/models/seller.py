from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Seller(Base):
    products = relationship('Product', secondary='prdseller')
    is_active = Column(Boolean, default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
