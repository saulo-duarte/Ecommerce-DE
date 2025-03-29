from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    street = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(String(20), nullable=False)
    country = Column(String(50), nullable=False)
    is_default = Column(Boolean, default=False)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(user_id={self.user_id}, city={self.city})>"
