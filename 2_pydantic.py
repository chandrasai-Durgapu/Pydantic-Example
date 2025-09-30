from pydantic import BaseModel

class Product(BaseModel):
    id: int
    price: float
    in_stock: bool

data={'id': 105,'price': 50.24, 'in_stock': False}

product=Product(**data)
print(product)