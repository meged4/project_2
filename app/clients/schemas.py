from pydantic import BaseModel, EmailStr


class SClientRegister(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class SClientLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
