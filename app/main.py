from fastapi import FastAPI
from .routers import auth, blog, users
import uvicorn

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
