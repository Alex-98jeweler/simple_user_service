from pydantic import BaseModel, validator, root_validator


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    age: int

    class Config:
        orm_mode=True