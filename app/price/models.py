from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String


class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    service = Column(String)
    cost = Column(Integer, nullable=False)

    schedule = relationship("Schedule", back_populates="price")

    def __str__(self):
        return f"{self.service}"
