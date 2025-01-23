from fastapi import FastAPI, HTTPException,Response
from typing import List
from model import Employee
from database import employee_helper,employee_collection
from pymongo import MongoClient, errors
import json

# FastAPI Instance
app = FastAPI()


@app.get("/employees", response_model=List[dict])
async def get_employees():
    try:
        print("Connecting to database...")
        employees = employee_collection.find()
        documents = []
        for document in employees:
            print(document)
            documents.append(document)

        # Use json library to encode the data
        json_data = json.dumps(documents) 
        print(json_data)
        return Response(content=json_data, media_type="application/json")        

    except errors.ServerSelectionTimeoutError as e:
        # Handles connection timeout errors
        print(f"Error connecting to database: {e}")
        raise HTTPException(status_code=500, detail="Could not connect to the database. Please try again later.")
    
    except errors.PyMongoError as e:
        # Handles other MongoDB errors
        print(f"MongoDB error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while querying the database.")
    
    except Exception as e:
        # Catch all other exceptions
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

"""

@app.get("/employees/{employee_id}", response_model=dict)
async def get_employee(employee_id: str):
    employee = employee_collection.find_one({"_id": ObjectId(employee_id)})
    if employee:
        return employee_helper(employee)
    raise HTTPException(status_code=404, detail="Employee not found")



@app.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: str):
    result = employee_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count:
        return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", response_model=dict)
async def create_employee(employee: Employee):
    employee_dict = employee.dict()
    result = employee_collection.insert_one(employee_dict)
    if result.inserted_id:
        return {"message": "Employee added successfully", "id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Failed to add employee")

"""    