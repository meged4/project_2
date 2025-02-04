from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import relationship


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))
    master_id = Column(Integer, ForeignKey("masters.id"))
    price_id = Column(Integer, ForeignKey('price.id'))
    date = Column(Date, nullable=False)
    time_start = Column(Time, nullable=False)
    time_finish = Column(Time, nullable=False)

    client = relationship("Clients", back_populates='schedule')
    master = relationship("Masters", back_populates='schedule')
    price = relationship("Price", back_populates="schedule")

    def __str__(self):
        return f"Запись № {self.id} на : {self.date} {self.time}"
