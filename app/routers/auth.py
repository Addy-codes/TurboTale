from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database
from ..utils import security
from bson import ObjectId
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=schema.UserInDB)
async def register(user: schema.UserCreate):
    existing_user = database.find_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = security.get_password_hash(user.password)
    user_data = user.dict()
    user_data['password'] = hashed_password
    new_user = database.add_user(user_data)
    return new_user

@router.post("/login", response_model=schema.Token)
async def login_for_access_token(user_credentials: OAuth2PasswordRequestForm = Depends()) -> schema.Token:
    user = database.find_user_by_username(user_credentials.username)
    if not user or not security.verify_password(user_credentials.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Generate a JWT token
    token = security.create_access_token(user['username'])
    return schema.Token(access_token= token, token_type= "bearer")
