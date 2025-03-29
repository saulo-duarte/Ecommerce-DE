from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.config.database import Base

class ProductReview(Base):
    __tablename__ = "product_reviews"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String(1000), nullable=True)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="reviews")
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="reviews")

    def __repr__(self):
        return f"<ProductReview(id={self.id}, rating={self.rating}, product_id={self.product_id}, user_id={self.user_id})>"
