from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Buyer(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
