from fastapi import FastAPI
from sqladmin import Admin
from app.database import engine
from app.admin.views import ClientsAdmin, MastersAdmin, PriceAdmin, ScheduleAdmin
from app.clients.router import router as clients_router
from app.masters.router import router as masters_router
from app.price.router import router as price_router
from app.schedule.router import router as schedule_router
from app.admin.auth import authentication_backend


app = FastAPI()
app.include_router(clients_router)
app.include_router(masters_router)
app.include_router(price_router)
app.include_router(schedule_router)

admin = Admin(app, engine=engine) #, authentication_backend=authentication_backend
admin.add_view(ClientsAdmin)
admin.add_view(MastersAdmin)
admin.add_view(PriceAdmin)
admin.add_view(ScheduleAdmin)


@app.get('/')
def get_home_page():
    return "HOME PAGE"
