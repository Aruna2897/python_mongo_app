from pymongo import MongoClient
from bson import ObjectId

# MongoDB Connection
client = MongoClient("mongodb://mongo:27017")
db = client["practice_db"]
employee_collection = db["employee"]

# Helper Function to Convert MongoDB Document to JSON
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "age": employee["age"],
        "position": employee["position"],
        "department": employee["department"],
        "salary": employee["salary"],
        "hire_date": employee["hire_date"],
        "skills": employee["skills"],
        "performance_rating": employee["performance_rating"],
    }
