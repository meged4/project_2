from pydantic import BaseModel


class SServiceInfo(BaseModel):
    service: str
    cost: int

    class Config:
        from_attributes = True
