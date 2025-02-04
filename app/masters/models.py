from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, Integer, Float


class Masters(Base):
    __tablename__ = 'masters'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    hashed_password = Column(String, nullable=False)
    rating = Column(Float, nullable=False, default=0)

    schedule = relationship("Schedule", back_populates="master")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"