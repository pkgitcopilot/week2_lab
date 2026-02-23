# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, high-performance REST APIs using the FastAPI framework. You'll practice creating endpoints, handling HTTP methods, managing request/response data, and deploying a functional web service that clients can interact with.

## 📝 Tasks

### 🛠️ Create a Basic Todo API

#### Description

Build a REST API for managing a simple todo list. Your API should support creating, reading, updating, and deleting todos (CRUD operations) with proper HTTP status codes and error handling.

#### Requirements

Completed program should:

- Set up a FastAPI application with proper imports and initialization
- Create a data model for todo items using Pydantic (with fields: id, title, description, completed)
- Implement GET endpoint to retrieve all todos
- Implement GET endpoint to retrieve a single todo by id
- Implement POST endpoint to create a new todo with validation
- Implement PUT endpoint to update an existing todo
- Implement DELETE endpoint to remove a todo
- Return appropriate HTTP status codes (200, 201, 404, 400)
- Include error handling for invalid requests

### 🛠️ Add Advanced Features and Testing

#### Description

Enhance your API with query parameters, filtering, and comprehensive testing to ensure reliability.

#### Requirements

Completed program should:

- Add query parameters to filter todos (e.g., by completion status)
- Implement pagination support for the todo list
- Add request validation with meaningful error messages
- Create unit tests for at least 5 endpoints
- Document your API with proper docstrings and FastAPI auto-generated documentation
- Run the API locally and verify all endpoints work correctly using a REST client (Postman, curl, or FastAPI's built-in docs)
