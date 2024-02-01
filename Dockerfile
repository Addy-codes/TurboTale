# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set the working directory in the container
WORKDIR /usr/src/blog-api

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Navigate to the app directory
# WORKDIR /usr/src/blog-api/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV MONGO_USERNAME=addy \
    MONGO_PASSWORD=admin%40123

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to hold the name of the application file
ENV UVICORN_APP="main:app"

# Run uvicorn when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
