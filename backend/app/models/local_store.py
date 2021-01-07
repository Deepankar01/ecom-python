from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class LocalStore(Base):
    name = Column(String, nullable=False)
    store_id = Column(UUID(as_uuid=True), ForeignKey("store.id"))
    address_id = Column(UUID(as_uuid=True), ForeignKey("address.id"))
    address = relationship('Address', backref="local_store", uselist=False)
    store = relationship('Store', backref="localStore", uselist=False)
    # products = relationship('Product', secondary="prdstore")
