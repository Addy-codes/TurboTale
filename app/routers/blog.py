from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database
from bson import ObjectId

router = APIRouter(tags=["Blogs"])

@router.post("/blog", response_model=schema.BlogInDB)
async def create_blog(blog: schema.BlogCreate):
    new_blog = database.add_blog(blog.dict())
    return new_blog

@router.get("/blogs", response_model=list[schema.BlogInDB])
async def get_all_blogs(limit: int = 10, skip: int = 0):
    blogs = database.get_all_blogs(limit, skip)
    return blogs

@router.get("/blog/{blog_id}", response_model=schema.BlogInDB)
async def get_blog(blog_id: str):
    blog = database.get_blog_by_id(ObjectId(blog_id))
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
