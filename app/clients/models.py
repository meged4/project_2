from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    schedule = relationship("Schedule", back_populates='client')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"