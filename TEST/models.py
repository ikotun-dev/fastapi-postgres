from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Biker(Base):
    __tablename__ = "Biker"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    firstname = Column(String(255), nullable=True)
    lastname = Column(String(255), nullable=True)
    password = Column(String(length=255))
    phone_number = Column(Boolean, default=False, nullable=True)
    email = Column(String, default=None, nullable=True)
    profile_image = Column(String(1000), nullable=True)
    created_at = Column(DateTime, default=datetime.now, server_default=func.now())

    posts = relationship("Post", back_populates="biker")

class Post(Base) : 
    __tablename__ = "Post"

    id = Column(Integer, primary_key=True)
    video_url = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now, server_default=func.now())
    location = Column(String(255), nullable=True)

    biker_id = Column(Integer, ForeignKey("Biker.id"))
    biker = relationship("Biker", back_populates="posts")