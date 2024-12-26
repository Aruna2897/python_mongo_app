from pydantic import BaseModel, Field
from typing import List

# Pydantic Model for Employee Validation
class Employee(BaseModel):
    name: str
    age: int
    position: str
    department: str
    salary: float
    hire_date: str
    skills: List[str] = Field(default_factory=list)
    performance_rating: float = Field(ge=0, le=5)
