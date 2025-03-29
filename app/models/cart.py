from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.config.database import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User")

    def __repr__(self):
        return f"<CartItem(id={self.id}, quantity={self.quantity}, price={self.price}, user_id={self.user_id})>"
