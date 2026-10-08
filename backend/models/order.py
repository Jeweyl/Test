from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, ForeignKey, Numeric
from datetime import datetime
from decimal import Decimal

from database import Base

class OrderItem(Base):
    __tablename__ = "orderitems"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id:Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order = relationship("Order", back_populates="order_items")
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    count: Mapped[int] = mapped_column(Integer, default=1)
    price:Mapped[Decimal] = mapped_column(Numeric(10, 2)) 
    
    def total_price(self):
        return self.price * self.count

class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user_id: Mapped[int] = mapped_column(Integer, default=1)
    order_items = relationship("OrderItem", back_populates="order")
    
    def total_price_for_order(self)->Decimal:
        total = Decimal("0")
        for order_item in self.order_items:
            total += order_item.total_price()
        return total