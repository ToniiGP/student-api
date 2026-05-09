# Student Management API

A REST API built with FastAPI and SQLite for managing student records.

## Tech Stack
- Python
- FastAPI
- SQLite

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /students | Get all students |
| GET | /students/{id} | Get a single student |
| POST | /students | Add a new student |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |

## Running Locally

1. Install dependencies: pip install fastapi uvicorn
2. Start the server: python -m uvicorn main:app --reload
3. Open your browser and go to: http://127.0.0.1:8000/docs   
This opens the interactive API documentation where you can test all endpoints.