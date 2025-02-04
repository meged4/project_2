from app.dao.base import BaseDAO
from app.schedule.models import Schedule
from app.database import async_session_maker
from sqlalchemy import select, and_, or_


class ScheduleDAO(BaseDAO):
    model = Schedule

    @classmethod
    async def get_schedule_for_client(cls, date, time_from, time_to):
        async with async_session_maker() as session:
            table = cls.model
            query = select(table).where(and_(table.date == date,
                                                 or_(and_(),
                                                     and_(),
                                                     and_()
                                                     )
                                                 )
                                            )
            res = await session.execute(query)
            return res.scalars().all()
