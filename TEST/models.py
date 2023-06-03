from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from datetime import datetime

class Biker(Base):
    __tablename__ = "Biker"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    # firstname = Column(String(255), nullable=True)
    # lastname = Column(String(255), nullable=True)
    password = Column(String(length=255))
    # phone_number = Column(Boolean, default=False, nullable=True)
    # email = Column(String, default=None, nullable=True)
    # profile_image = Column(String(1000), nullable=True)
    # created_at = Column(DateTime, default=datetime.now, server_default=func.now())

