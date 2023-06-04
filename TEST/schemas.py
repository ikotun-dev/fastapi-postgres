from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Biker(BaseModel):
    id: Optional[int]
    username: str = Field(..., max_length=255, unique=True)
    firstname: Optional[str] = Field(max_length=255)
    lastname: Optional[str] = Field(max_length=255)
    password: str = Field(..., max_length=255)
    phone_number: Optional[int] 
    email: Optional[str]
    profile_image:  Optional[str] 
    created_at: Optional[datetime] =  Field(default_factory=datetime.now)
    club: Optional[bool] = False
    badge: Optional[bool] = False
    location: Optional[str] = None
    about_me: Optional[str] = None
    following: Optional[List[int]] = []
    followers_count: Optional[int] = 0
    following_count: Optional[int] = 0 
    max_speed: Optional[int] = None
    confirmation_code: Optional[int] = None
    verification_status: Optional[bool] = False




 