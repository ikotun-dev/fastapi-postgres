from pydantic import BaseModel
import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


#user model
class User(BaseModel):
    id: Optional[UUID]= uuid4()
    first_name: str 
    last_name: str
    gender: Gender
    role: List[Role]


 