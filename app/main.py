from fastapi import FastAPI
from .routers import auth, blog, users

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API"}
