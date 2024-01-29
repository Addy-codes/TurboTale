from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database
from bson import ObjectId

router = APIRouter(tags=["Blogs"])

@router.post("/blog", response_model=schemas.BlogInDB)
async def create_blog(blog: schemas.BlogCreate):
    new_blog = await database.add_blog(blog.dict())
    return new_blog

@router.get("/blogs", response_model=list[schemas.BlogInDB])
async def get_all_blogs(limit: int = 10, skip: int = 0):
    blogs = await database.get_all_blogs(limit, skip)
    return blogs

@router.get("/blog/{blog_id}", response_model=schemas.BlogInDB)
async def get_blog(blog_id: str):
    blog = await database.get_blog_by_id(ObjectId(blog_id))
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
