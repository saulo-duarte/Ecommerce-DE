from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.config.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    status = Column(String(50), default="pending")
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User")

    items = relationship("OrderItem", back_populates="order")

    payment = relationship("Payment", back_populates="order", uselist=False)

    def __repr__(self):
        return f"<Order(id={self.id}, total_amount={self.total_amount}, user_id={self.user_id}, status={self.status})>"
