from app.dao.base import BaseDAO
from app.masters.models import Masters
from app.database import async_session_maker
from sqlalchemy import select


class MastersDAO(BaseDAO):
    model = Masters

    @classmethod
    async def find_by_phone(cls, number):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(phone_number=number)
            res = await session.execute(query)
            return res.scalar_one_or_none()
