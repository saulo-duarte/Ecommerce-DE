from pydantic import BaseModel
from datetime import datetime
from typing import List
from .cart_item import CartItemResponse

class CartBase(BaseModel):
    user_id: int
    is_active: bool = True

class CartCreate(CartBase):
    pass

class CartResponse(CartBase):
    id: int
    created_at: datetime
    items: List[CartItemResponse] = []

    class Config:
        from_attributes = True
