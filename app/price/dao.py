from app.dao.base import BaseDAO
from app.price.models import Price
from app.database import async_session_maker
from sqlalchemy import insert, select, func


class PriceDAO(BaseDAO):
    model = Price

    @classmethod
    async def add_new_service(cls, service, cost):
        async with async_session_maker() as session:
            query = insert(cls.model).values(service=service, cost=cost).returning(cls.model)
            res = await session.execute(query)
            await session.commit()
            return res.scalar()

    @classmethod
    async def find_by_service_name(cls, name):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.service.contains("%Маникюр%"))
            res = await session.execute(query)
            return res.scalars().all()
