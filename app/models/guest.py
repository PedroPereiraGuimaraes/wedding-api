from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Dependent(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    confirmed: bool = Field(...)

class Guest(BaseModel):
    accountable: str = Field(..., max_length=100)
    token: str = Field(...)
    age: int = Field(...)
    email: EmailStr = Field(...)
    confirmed: bool = Field(...)
    dependents: List[Dependent] = Field(...)
    
    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

    def __repr__(self):
        return f"Guest({self.accountable}, {self.email}, {len(self.dependents)} dependents)"