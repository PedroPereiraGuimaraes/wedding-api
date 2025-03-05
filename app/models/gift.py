from pydantic import BaseModel, EmailStr, Field
from typing import List

class Gift(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(...)
    price: float = Field(...)
    link: str = Field(...)
    
    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

    def __repr__(self):
        return f"Gift({self.name}, {self.description}, {self.price}, {self.link})"
    
    def to_dict(self):
        return self.model_dump()