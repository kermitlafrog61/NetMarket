from sqlalchemy import Column, Integer, String, DateTime, Float, func
from core.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(128))
    description = Column(String(256))
    price = Column(Float(2))
    created_at = Column(DateTime, default=func.now())
    # TODO: add image
