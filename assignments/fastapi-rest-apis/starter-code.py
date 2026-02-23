"""
FastAPI REST API Starter Code
Build a todo management API with FastAPI

TODO: Complete the implementation by following the assignment requirements
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple REST API for managing todos",
    version="1.0.0"
)

# Define the Pydantic model for todos
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for todos (for demonstration purposes)
todos_db: List[Todo] = [
    Todo(id=1, title="Learn FastAPI", description="Complete the FastAPI assignment", completed=False),
    Todo(id=2, title="Build a REST API", description="Create CRUD endpoints", completed=False),
]

# TODO: Implement the following endpoints:
# 1. GET /todos - Retrieve all todos
# 2. GET /todos/{todo_id} - Retrieve a specific todo
# 3. POST /todos - Create a new todo
# 4. PUT /todos/{todo_id} - Update a todo
# 5. DELETE /todos/{todo_id} - Delete a todo

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo API!"}

# Add your endpoint implementations below
# Remember to use the appropriate HTTP methods and status codes
