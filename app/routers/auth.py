from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database
from ..utils import security
from bson import ObjectId

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=schemas.UserInDB)
async def register(user: schemas.UserCreate):
    existing_user = await database.find_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = security.hash_password(user.password)
    user_data = user.dict()
    user_data['password'] = hashed_password
    new_user = await database.add_user(user_data)
    return new_user

@router.post("/login", response_model=schemas.Token)
async def login(user_credentials: schemas.UserCreate):
    user = await database.find_user_by_email(user_credentials.email)
    if not user or not security.verify_password(user_credentials.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Generate a JWT token
    token = security.create_access_token(data={"sub": user['email']})
    return {"access_token": token, "token_type": "bearer"}