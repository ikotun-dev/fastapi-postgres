from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime, timezone
from enum import Enum
class Biker(BaseModel):
    id: Optional[int]
    username: str = Field(..., max_length=255, unique=True)
    firstname: Optional[str] = Field(max_length=255)
    lastname: Optional[str] = Field(max_length=255)
    password: str = Field(..., max_length=255)
    phone_number: Optional[int] 
    email: Optional[str]
    profile_image:  Optional[str] 
    # created_at: Optional[datetime] =  Field(default_factory=utc.now)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
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

class PostType(Enum):
    video  = "video"
    image = "image"

class Post(BaseModel):
     id: Optional[int]
#     # CONNECTION BETWEEN BIKER AND POST
#     biker_id = models.ForeignKey(Biker, on_delete=models.CASCADE)
     post_type: Optional[PostType]
     biker_id : int 
     video_url: str # url field
     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
     location: str = Field(max_length=255)

 