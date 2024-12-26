from fastapi import FastAPI, HTTPException, Response
from typing import List
from pydantic import BaseModel  

from model import Employee  
from database import employee_helper, employee_collection  

# FastAPI Instance
app = FastAPI()


@app.get("/employees", response_model=List[dict])
async def get_employees():
    """
    Retrieves all employee records from the database.

    Raises:
        HTTPException: 500 Internal Server Error if a database error occurs.
    """
    try:
        employees = employee_collection.find()
        documents = [employee_helper(document) for document in employees] 
        return documents
    except Exception as e:
        print(f"Error retrieving employees: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while retrieving employees.")


@app.get("/employees/{employee_id}", response_model=dict)
async def get_employee(employee_id: str):
    """
    Retrieves a specific employee record by ID.

    Args:
        employee_id (str): The ID of the employee to retrieve.

    Raises:
        HTTPException: 404 Not Found if the employee is not found.
        HTTPException: 500 Internal Server Error if a database error occurs.
    """
    try:
        employee = employee_collection.find_one({"_id": ObjectId(employee_id)})
        if employee:
            return employee_helper(employee)
        raise HTTPException(status_code=404, detail="Employee not found")
    except Exception as e:
        print(f"Error retrieving employee with ID {employee_id}: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while retrieving the employee.")


@app.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: str):
    """
    Deletes a specific employee record by ID.

    Args:
        employee_id (str): The ID of the employee to delete.

    Raises:
        HTTPException: 404 Not Found if the employee is not found.
        HTTPException: 500 Internal Server Error if a database error occurs.
    """
    try:
        result = employee_collection.delete_one({"_id": ObjectId(employee_id)})
        if result.deleted_count:
            return {"message": "Employee deleted successfully"}
        raise HTTPException(status_code=404, detail="Employee not found")
    except Exception as e:
        print(f"Error deleting employee with ID {employee_id}: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while deleting the employee.")


@app.post("/employees", response_model=dict)
async def create_employee(employee: Employee):
    """
    Creates a new employee record in the database.

    Args:
        employee (Employee): The employee data to be added.

    Raises:
        HTTPException: 500 Internal Server Error if a database error occurs.
    """
    try:
        employee_dict = employee.dict()
        result = employee_collection.insert_one(employee_dict)
        if result.inserted_id:
            return {"message": "Employee added successfully", "id": str(result.inserted_id)}
        raise HTTPException(status_code=500, detail="Failed to add employee")
    except Exception as e:
        print(f"Error creating employee: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while creating the employee.")