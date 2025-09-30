from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at: datetime
    address: Address
    tags: List[str] = []


# Create User instance
user = User(
    id= 1,
    name= "chandra",
    is_active= True,
    created_at=datetime(2024,3,15,14,30),
    address=Address(
        street="my area",
        city="hyderabad",
        zip_code="5000871",
                    ),
    tags=[
        "premium",
        "subscriber"
        ],

        model_config=ConfigDict(
            json_encoders={
                datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
            }
        )
        )


# model_dump()-> dict
python_dict = user.model_dump()
print(python_dict)
print("\n")

# model_dump_json()
json_str= user.model_dump_json()
print(json_str)

