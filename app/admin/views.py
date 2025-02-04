from sqladmin import ModelView
from app.clients.models import Clients
from app.schedule.models import Schedule
from app.masters.models import Masters
from app.price.models import Price


class ClientsAdmin(ModelView, model=Clients):
    name = "Клиент"
    name_plural = "Клиенты"
    icon = 'fa-solid fa-user'
    column_searchable_list = [Clients.first_name, Clients.last_name]
    column_details_exclude_list = [Clients.hashed_password]
    column_exclude_list = [Clients.hashed_password]


class MastersAdmin(ModelView, model=Masters):
    name = "Мастер"
    name_plural = "Мастера"
    icon = 'fa-solid fa-user'
    column_exclude_list = [Masters.hashed_password]
    column_details_exclude_list = [Masters.hashed_password]
    column_searchable_list = [Masters.first_name, Masters.last_name]


class PriceAdmin(ModelView, model=Price):
    name = "Прайс"
    name_plural = "Прайс"
    column_list = [c.name for c in Price.__table__.c] + [Price.schedule]


class ScheduleAdmin(ModelView, model=Schedule):
    name = "Расписание"
    name_plural = "Расписание"
    column_list = [c.name for c in Schedule.__table__.c] + [Schedule.client, Schedule.master, Schedule.price]
    column_searchable_list = [Schedule.date]