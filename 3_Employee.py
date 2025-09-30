from pydantic import BaseModel,Field
from typing import Optional

class Employee(BaseModel):
    id : int
    name: str = Field(...,
                      min_length=3, max_length=50, description="Employee Name", example="chandra sai")
    department: Optional[str]= 'General'
    salary: float = Field(...,
                          ge=10000)
    

data2={ 'id': 108, 'name': 'chandra', 'salary': 20000}

employee=Employee(**data2)
print(employee)