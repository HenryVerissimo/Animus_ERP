from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date

from .base import Base


class Product(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    purchase_price = Column(Float, nullable=False)
    description = Column(String(300), nullable=True)
    created_in = Column(Date, nullable=True, default=date.today())
    status = Column(String(15), default="disponível")
