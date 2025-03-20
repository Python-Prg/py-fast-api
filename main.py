from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime, timezone
from typing import List, Dict

# Initialize FastAPI app
app = FastAPI(
    title="Employee API",
    description="A FastAPI-based Employee Management System",
    version="1.0.0"
)

# In-memory Employee Data
employees: List[Dict] = [
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
    }
]

# Pydantic Models
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    user_id: int
    created_at: str  # Using string format for JSON compatibility
    modified_at: str

    class Config:
        from_attributes = True

# API Routes
@app.get("/", tags=["General"])
async def root():
    return {"message": "Welcome to Employee Management API"}

@app.get("/employees", response_model=List[EmployeeResponse], tags=["Employees"])
async def get_employees():
    return employees

@app.get("/employees/{user_id}", response_model=EmployeeResponse, tags=["Employees"])
async def get_employee(user_id: int):
    employee = next((emp for emp in employees if emp["user_id"] == user_id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees", response_model=EmployeeResponse, tags=["Employees"])
async def create_employee(employee: EmployeeCreate):
    new_id = max(emp["user_id"] for emp in employees) + 1 if employees else 1
    created_at = modified_at = datetime.now(timezone.utc).isoformat()

    new_employee = {
        "user_id": new_id,
        **employee.model_dump(),
        "created_at": created_at,
        "modified_at": modified_at
    }

    employees.append(new_employee)
    return new_employee

@app.put("/employees/{user_id}", response_model=EmployeeResponse, tags=["Employees"])
async def update_employee(user_id: int, employee: EmployeeUpdate):
    for emp in employees:
        if emp["user_id"] == user_id:
            emp.update({
                **employee.model_dump(),
                "modified_at": datetime.now(timezone.utc).isoformat()
            })
            return emp

    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{user_id}", tags=["Employees"])
async def delete_employee(user_id: int):
    global employees
    employees = [emp for emp in employees if emp["user_id"] != user_id]
    return {"message": "Employee deleted successfully"}
