from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_master
from app.exceptions import NotFindService
from app.price.dao import PriceDAO
from app.price.schemas import SServiceInfo

router = APIRouter(prefix="/service",
                   tags=['Услуги'])


@router.post('/add_service')
async def add_service_by_master(service: SServiceInfo, master=Depends(get_current_master)):
    new_service = await PriceDAO.add_new_service(service.service, service.cost)
    return f"Master {master.first_name} добавила новую услугу: {new_service.service}"


@router.get('/find_service')
async def find_service_by_client(name: str):
    search_service = await PriceDAO.find_by_service_name(name)
    if not search_service:
        raise NotFindService
    return search_service
