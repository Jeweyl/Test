from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric

from database import Base

class Products(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type = String(255), nullable=False)
    price: Mapped[int] = mapped_column(type = Numeric(10, 2), nullable=False)
