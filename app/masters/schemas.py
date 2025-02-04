from pydantic import BaseModel


class SMastersLogin(BaseModel):
    phone_number: str
    password: str

    class Config:
        from_attributes = True


class SMasterRegister(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    password: str
    rating: float
