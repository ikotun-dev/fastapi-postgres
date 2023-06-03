from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Biker(BaseModel):
    id: int
    username: str = Field(..., max_length=255, unique=True)
    firstname: str = Field(None, max_length=255)
    lastname: str = Field(None, max_length=255)
    password: str
    phone_number: int = 0
    email: str = None
    profile_image:  str 
    created_at: datetime =  Field(default_factory=datetime.now())
    club: bool = False
    badge: bool = False
    location: str = None
    about_me: str = None
    following: List[int] = []
    followers_count: int = 0
    following_count: int = 0 
    max_speed: int = None
    confirmation_code: int = None
    verification_status: bool = False




 