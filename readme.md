
# Turbo-Tale

## Description
This Turbo-Tale is a FastAPI-based web service designed to provide a backend for blog applications. It offers a range of functionalities including user authentication, creating, editing, and retrieving blog posts, and user management.

## API Docs:

![image](https://github.com/Addy-codes/TurboTale/assets/72205091/5a64804c-6449-4e26-a49c-7343b93837fa)


![image](https://github.com/Addy-codes/TurboTale/assets/72205091/3ffb639a-6940-4b99-bdc3-8ff0f74e9bac)



## Running the API Locally
To run the API locally, follow these steps:

### Prerequisites
- Python 3.9
- pip (Python package manager)

### Setup and Installation
1. **Clone the Repository**
   ```
   git clone https://github.com/Addy-codes/TurboTale.git
   cd blog-api
   ```

2. **Set Up a Virtual Environment**
   - For Windows:
     ```
     python -m venv my_venv
     .\my_venv\Scripts\activate
     ```
   - For Unix or MacOS:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory and add the following:
   ```
   MONGO_USERNAME=your_username
   MONGO_PASSWORD=your_password
   ```

5. **Run the Application**
   ```
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## Running with Docker
To run the API using Docker Compose, follow these steps:

1. **Build and Run with Docker Compose**
   ```
   docker-compose up -d --build
   ```

2. **Access the Application**
   The API will be available at `http://localhost:8000`, and you can visit the API documentation at `http://localhost:8000/docs`.

## Deployed API
The API is deployed on Render and can be accessed at [https://turbotale.onrender.com/](https://turbotale.onrender.com/).

To test the API and view its documentation, visit [https://turbotale.onrender.com/docs](https://turbotale.onrender.com/docs).

# API Endpoints

## General

- `GET /`
  - Description: Root endpoint that provides a welcome message.

## Authentication

- `POST /register`
  - Description: Register a new user.

- `POST /login`
  - Description: Authenticate a user and return a token.

## Blog Routes

- `POST /blog`
  - Description: Create a new blog post.

- `GET /blogs`
  - Description: Retrieve all blog posts with pagination.
  - Query Parameters: 
    - `page_no`: Page number (integer, greater than or equal to 1).
    - `records_per_page`: Number of blog posts per page (integer, up to 100).

- `GET /blog/{blog_id}`
  - Description: Retrieve a specific blog post by ID.
  - Path Parameters:
    - `blog_id`: Blog post ID.

- `PATCH /blog/{blog_id}`
  - Description: Update a specific blog post by ID.
  - Path Parameters:
    - `blog_id`: Blog post ID.

- `DELETE /blog/{blog_id}`
  - Description: Delete a specific blog post by ID.
  - Path Parameters:
    - `blog_id`: Blog post ID.

- `GET /dashboard`
  - Description: Retrieve blog posts that match the criteria of the current user.
  - Query Parameters: 
    - `page_no`: Page number (integer, greater than or equal to 1).
    - `records_per_page`: Number of blog posts per page (integer, up to 100).

## User Routes

- `PUT /updateUser/`
  - Description: Update user information.

- `PATCH /update-tags`
  - Description: Update user's tags.
