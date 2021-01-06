from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class StoreManager(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    store_id = Column(UUID(as_uuid=True), ForeignKey("store.id"), unique=True)
    user = relationship('User')
