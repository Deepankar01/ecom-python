from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Category(Base):
    parent_id = Column(UUID(as_uuid=True), ForeignKey('category.id'))
    name = Column(String)
    children = relationship("Category")
