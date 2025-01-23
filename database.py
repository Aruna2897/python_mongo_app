from pymongo import MongoClient
from bson import ObjectId
from typing import Dict, Any

# MongoDB Connection
client = MongoClient("mongodb://mongo:27017")
db = client["practice_db"]
employee_collection = db["employee"]



def employee_helper(employee: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": str(employee.get("_id", "")),
        "name": employee.get("name", "Unknown"),
        "age": employee.get("age", 0),
        "position": employee.get("position", "Unknown"),
        "department": employee.get("department", "Unknown"),
        "salary": employee.get("salary", 0.0),
        "hire_date": employee.get("hire_date", "Unknown"),
        "skills": employee.get("skills", []),
        "performance_rating": employee.get("performance_rating", "Unknown"),
    }
