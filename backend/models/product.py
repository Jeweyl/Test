from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric

from decimal import Decimal

from database import Base

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[str|None] = mapped_column(String(500), nullable=True)