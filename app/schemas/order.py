from pydantic import BaseModel
from typing import List
from datetime import datetime
from ordem_item import OrderItemResponse

class OrderBase(BaseModel):
    total_amount: float
    status: str = "pending"

class OrderCreate(OrderBase):
    user_id: int
    items: List[OrderItemResponse]

class OrderResponse(OrderBase):
    id: int
    user_id: int
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True
