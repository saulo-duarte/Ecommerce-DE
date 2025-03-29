from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    device_type = Column(String(50), nullable=False)
    device_model = Column(String(100))
    last_login = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="devices")

    def __repr__(self):
        return f"<Device(user_id={self.user_id}, type={self.device_type})>"
