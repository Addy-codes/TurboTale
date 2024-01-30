from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schema, database
from bson import ObjectId
from ..utils import security

router = APIRouter(tags=["Blogs"])

@router.post("/blog", response_model=schema.BlogInDB)
async def create_blog(blog: schema.BlogCreate, current_user: schema.UserInDB = Depends(security.get_current_user)):
    new_blog = database.add_blog(blog.dict())
    return new_blog

@router.get("/blogs", response_model=list[schema.BlogInDB])
async def get_all_blogs(limit: int = 10, skip: int = 0):
    blogs = database.get_all_blogs(limit, skip)
    return blogs

@router.get("/blog/{blog_id}", response_model=schema.BlogInDB)
async def get_blog(blog_id: str, current_user: schema.UserInDB = Depends(security.get_current_user)):
    blog = database.get_blog_by_id(ObjectId(blog_id))
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.patch("/blog/{blog_id}", response_model=schema.BlogInDB)
async def update_blog(blog_id: str, blog_update: schema.BlogUpdate, current_user: schema.UserInDB = Depends(security.get_current_user)):
    blog = database.get_blog_by_id(blog_id)
    if blog['author_id'] != current_user['id']:
        raise HTTPException(status_code=401, detail="You cannot change this blog since you're not the author")
    updated_blog = database.update_blog(blog_id, blog_update.dict(exclude_unset=True))
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog
    

@router.delete("/blog/{blog_id}", status_code=204)
async def delete_blog(blog_id: str):
    if not database.delete_blog(blog_id):
        raise HTTPException(status_code=404, detail="Blog not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
