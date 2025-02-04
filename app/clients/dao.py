from app.dao.base import BaseDAO
from app.clients.models import Clients
from app.database import async_session_maker
from sqlalchemy import select, func, insert


class ClientsDAO(BaseDAO):
    model = Clients

    @classmethod
    async def find_client(cls, email):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(email=email)
            res = await session.execute(query)
            return res.scalar_one_or_none()
