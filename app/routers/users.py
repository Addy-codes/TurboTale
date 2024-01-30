from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database
from bson import ObjectId
from ..utils import security

router = APIRouter(tags=["Users"])

@router.put("/user/{user_id}", response_model=schema.UserInDB)
async def update_user(user_id: str, user: schema.UserUpdate, current_user: schema.UserInDB = Depends(security.get_current_user)):
    updated_user = database.update_user(ObjectId(user_id), user.dict(exclude_unset=True))
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.patch("/user/{user_id}/tags", response_model=schema.UserInDB)
async def update_user_tags(user_id: str, tags: list[str], current_user: schema.UserInDB = Depends(security.get_current_user)):
    updated_user = database.update_user_tags(ObjectId(user_id), tags)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
