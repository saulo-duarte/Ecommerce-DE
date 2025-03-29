from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    card_number = Column(String(16), nullable=False)
    card_holder_name = Column(String(150), nullable=False)
    expiration_date = Column(String(7), nullable=False)
    brand = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="cards")

    def __repr__(self):
        return f"<Card(user_id={self.user_id}, brand={self.brand})>"