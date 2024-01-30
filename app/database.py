from pymongo import MongoClient
from pymongo.collection import Collection
from typing import List
from bson import ObjectId

# Configuration for MongoDB connection
MONGO_DETAILS = "mongodb+srv://addy:admin%40123@cluster0.wwsdot7.mongodb.net/"  # Replace with your MongoDB connection string

client = MongoClient(MONGO_DETAILS)

# Database and Collections
db = client.blog_db
user_collection = db.get_collection("users")
blog_collection = db.get_collection("blogs")

# Helper functions for User collection
def user_helper(user) -> dict:
    """Convert a user document to a dictionary."""
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        # "tags": user["tags"],
        # Add more fields as required
    }

def add_user(user_data: dict) -> dict:
    """Add a new user to the database."""
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    print(user.inserted_id)
    return user_helper(new_user)

def find_user_by_email(email: str) -> dict:
    """Find a user by ID."""
    user = user_collection.find_one({"email": email})
    if user:
        return user_helper(user)

def find_user(user_id: str) -> dict:
    """Find a user by ID."""
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)

# More user-related database functions...

# Helper functions for Blog collection
def blog_helper(blog) -> dict:
    """Convert a blog document to a dictionary."""
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author_id": blog["author_id"],
        "tags": blog["tags"],
        # Add more fields as required
    }

def add_blog(blog_data: dict) -> dict:
    """Add a new blog to the database."""
    blog = blog_collection.insert_one(blog_data)
    new_blog = blog_collection.find_one({"_id": blog.inserted_id})
    return blog_helper(new_blog)

def get_all_blogs(limit: int, skip: int) -> List[dict]:
    """Retrieve all blogs with pagination."""
    blogs = blog_collection.find().skip(skip).limit(limit)
    return [blog_helper(blog) for blog in blogs]

def get_blog_by_id(blog_id: str) -> dict:
    """Retrieve a specific blog by ID."""
    blog = blog_collection.find_one({"_id": ObjectId(blog_id)})
    if blog:
        return blog_helper(blog)

def get_blogs_by_user_tags(user_tags: List[str], limit: int, skip: int) -> List[dict]:
    """Fetch blogs matching user's followed tags with pagination."""
    blogs = blog_collection.find({"tags": {"$in": ObjectId(user_tags)}}).sort("relevance", -1).skip(skip).limit(limit)
    return [blog_helper(blog) for blog in blogs]

def update_blog(blog_id: str, updated_data: dict) -> dict:
    """Update an existing blog."""
    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$set": updated_data})
    updated_blog = blog_collection.find_one({"_id": ObjectId(blog_id)})
    if updated_blog:
        return blog_helper(updated_blog)

def delete_blog(blog_id: str) -> bool:
    """Delete a blog."""
    result = blog_collection.delete_one({"_id": ObjectId(blog_id)})
    return result.deleted_count > 0

# data = {
#     "username": "test3",
#     "email": "test3@gmail.com",
#     "password": "123456",
#     "tags": "chess"
# }

# print(add_user(data))
# Output: {'id': '65b7e12a1f24f9710ea6557a', 'username': 'test1', 'email': 'test1@gmail.com', 'tags': 'chess'}

# print(find_user('65b7e32153b27e34a9b3a45e'))

# blog = {
#     "title": "Chess",
#     "content": "Anish Giri is the chess GOAT!",
#     "tags": "chess",
#     "author_id": "65b7e32153b27e34a9b3a45e"
# }

# print(add_blog(blog))

# print(get_all_blogs(2,2))

# print(update_blog("65b7f923a1482f2e5aa931bc", {"content": "Anish Giri is the wittiest chess player!"}))

# print(delete_blog("65b7f866129562b7d80120bb"))