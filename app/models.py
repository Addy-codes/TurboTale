from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from bson import ObjectId
from datetime import datetime

# Helper to handle MongoDB ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# User Model
class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    username: str
    email: EmailStr
    password: str
    tags: List[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "username": "user123",
                "email": "user123@example.com",
                "password": "hashedpassword",
                "tags": ["coding", "chess"]
            }
        }

# Blog Model
class Blog(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: str
    content: str
    author_id: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime]
    tags: List[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "title": "Chess today",
                "content": "Magnus Carlsen is the Highest rated chess player",
                "tags": ["Chess", "Magnus"],
                "author_id": "65b89bf3ce0aef465a8330cd"
            }
        }
