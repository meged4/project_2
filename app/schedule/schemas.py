from pydantic import BaseModel
from datetime import date, time, datetime, timedelta
from typing import Optional
from fastapi import Query


class SScheduleGet:
    def __init__(self,
                 date: date = Query(..., description=f"Например, {datetime.now().date()}"),
                 time_start: time = Query(..., description=f"Например, {datetime.now().time().strftime('%H:%M')}"),
                 time_finish: time = Query(..., description=f"Например, {datetime.now().time().strftime('%H:%M')}")):
        self.date = date
        self.time_start = time_start
        self.time_finish = time_finish
