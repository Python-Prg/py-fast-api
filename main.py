from pickle import EMPTY_LIST

from fastapi import FastAPI

app = FastAPI()

Employee=[
  {
    "user_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "created_at": "2024-03-21T10:15:30Z",
    "modified_at": "2024-03-21T12:45:00Z"
  },
  {
    "user_id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "created_at": "2024-03-20T14:30:00Z",
    "modified_at": "2024-03-21T09:00:00Z"
  },
  {
    "user_id": 3,
    "first_name": "Alice",
    "last_name": "Brown",
    "email": "alice.brown@example.com",
    "created_at": "2024-03-19T08:20:15Z",
    "modified_at": "2024-03-20T16:10:45Z"
  }
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/employee")
async def get_employees():
    return Employee