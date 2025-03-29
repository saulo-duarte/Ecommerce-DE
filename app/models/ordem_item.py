from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product")
    
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="items")

    def __repr__(self):
        return f"<OrderItem(id={self.id}, quantity={self.quantity}, price={self.price}, order_id={self.order_id})>"
