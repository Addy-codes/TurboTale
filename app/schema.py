from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# Schemas for User operations

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    username: str
    password: str
    tags: Optional[List[str]] = Field(
        [], example=["coding", "photography"])

class UserLogin(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    tags: Optional[List[str]] = None

class UserInDB(UserBase):
    id: str
    tags: List[str] = []

    class Config:
        orm_mode = True

class UpdateUserTags(BaseModel):
    add_tags: List[str] = Field(..., example=["Python", "Web Development"])
    remove_tags: List[str] = Field(..., example=["Python", "Web Development"])


# Schemas for Blog operations

class BlogBase(BaseModel):
    title: str
    content: str
    author_id: str

class BlogCreate(BlogBase):
    tags: Optional[List[str]] = []

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None

class BlogInDB(BlogBase):
    id: str
    author_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[str] = []

    class Config:
        orm_mode = True

# Schemas for Authentication

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None