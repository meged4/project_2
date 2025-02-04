from sqlalchemy import select, insert, func
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(kwargs)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_one(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            res = await session.execute(query)
            return res.scalar_one_or_none()





