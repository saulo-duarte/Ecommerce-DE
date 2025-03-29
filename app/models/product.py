from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean,
    ForeignKey, 
    Float
)
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.config.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(1000), nullable=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")

    reviews = relationship("ProductReview", back_populates="product")

    def __repr__(self):
        return f"""<Product(id={self.id}, 
            name={self.name}, 
            price={self.price}, 
            stock_quantity={self.stock_quantity})
        >"""
