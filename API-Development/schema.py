from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published:bool = True
    
class PostCreate(PostBase):
    pass
    
class UserOut(BaseModel):
   id:int 
   email:EmailStr
   created_at: datetime
   model_config = ConfigDict(from_attributes=True) # This replaces orm_mode=True

class Post(PostBase):
    id:int
    created_at:datetime
    user_id:int
    owner:UserOut
    model_config = ConfigDict(from_attributes=True) # This replaces orm_mode=True
    
class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserLogIn(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[int]=None