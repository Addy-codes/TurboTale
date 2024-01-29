from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database
from bson import ObjectId

router = APIRouter(tags=["Users"])

@router.put("/user/{user_id}", response_model=schemas.UserInDB)
async def update_user(user_id: str, user: schemas.UserUpdate):
    updated_user = await database.update_user(ObjectId(user_id), user.dict(exclude_unset=True))
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.patch("/user/{user_id}/tags", response_model=schemas.UserInDB)
async def update_user_tags(user_id: str, tags: list[str]):
    updated_user = await database.update_user_tags(ObjectId(user_id), tags)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
