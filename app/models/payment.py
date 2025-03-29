from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.config.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    method = Column(String(50), nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="payment")

    def __repr__(self):
        return f"<Payment(id={self.id}, amount={self.amount}, method={self.method}, status={self.status}, order_id={self.order_id})>"
