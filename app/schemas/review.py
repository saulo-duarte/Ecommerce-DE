from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductReviewBase(BaseModel):
    rating: float
    review_text: Optional[str] = None

class ProductReviewCreate(ProductReviewBase):
    product_id: int
    user_id: int

class ProductReviewResponse(ProductReviewBase):
    id: int
    product_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True