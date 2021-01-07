from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Seller(Base):
    # products = relationship('Product', secondary='prdseller')
    is_active = Column(Boolean, default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    store = relationship('Store', backref="seller")
    name_on_income_tax = Column(String, nullable=False)
    buisness_name = Column(String, nullable=False)
    buisness_address_id = Column(UUID(as_uuid=True), ForeignKey("address.id"))
    buisness_address = relationship('Address')
    tax_id = Column(String, nullable=False)
