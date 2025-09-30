from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']]=None

Comment.model_rebuild()

address= Address(
    street= "chandra mouli nagar",
    city= "Hyderabad",
    postal_code="5000871"
)

user= User(
    id= 1,
    name= "Chandra",
    address=address
)


comment= Comment(
    id =1,
    content="First Comment",
    replies=[
        Comment(
            id = 2,
            content="reply 1"
        ),
        Comment(
            id = 3,
            content="reply 2"
        )
    ]
)

