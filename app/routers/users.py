from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database
from bson import ObjectId
from ..utils import security

router = APIRouter(tags=["Users"])

@router.put("/updateUser/", response_model=schema.UserInDB)
async def update_user(user: schema.UserUpdate, current_user: schema.UserInDB = Depends(security.get_current_user)):
    existing_user = database.find_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    user_id = current_user['id']
    updated_user = database.update_user(ObjectId(user_id), user.dict(exclude_unset=True))
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# @router.patch("/user/{user_id}/tags", response_model=schema.UserInDB)
# async def update_user_tags(tags: list[str], current_user: schema.UserInDB = Depends(security.get_current_user)):
#     user_id = current_user['id']
#     updated_user = database.update_user_tags(ObjectId(user_id), tags)
#     if updated_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return updated_user

@router.patch("/update-tags", response_model=schema.UserInDB)
async def update_user_tags(tags: schema.UpdateUserTags, current_user: schema.UserInDB = Depends(security.get_current_user)):
    user_id = current_user["id"]
    # print(user_id)
    update_data = {}
    update_data['add_tags'] = tags.add_tags
    update_data['remove_tags'] = tags.remove_tags
    updated_user = database.update_tags(str(user_id), update_data)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {**updated_user, "id": user_id}
