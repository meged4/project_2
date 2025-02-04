from fastapi import APIRouter, Depends

from app.exceptions import NotFindVacantEntriesException
from app.schedule.dao import ScheduleDAO
from app.schedule.schemas import SScheduleGet
from app.auth.dependencies import get_current_client


router = APIRouter(prefix="/schedule",
                   tags=["Расписание"])


@router.get("/get_schedule")
async def get_schedule(info: SScheduleGet = Depends()):
    result = await ScheduleDAO.get_schedule_for_client(date=info.date,
                                                       time_from=info.time_start,
                                                       time_to=info.time_finish)
    if not result:
        raise NotFindVacantEntriesException
    return result


@router.get("/book_appointment")
async def book_appointment(info: SScheduleGet = Depends(), client=Depends(get_current_client)):
    return 1
