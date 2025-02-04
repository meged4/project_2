from fastapi import APIRouter, Response
from app.auth.auth import get_password_hash
from app.auth.auth import verify_password, create_access_token
from app.clients.dao import ClientsDAO
from app.clients.schemas import SClientRegister, SClientLogin
from app.exceptions import ClientAlreadyExistsException, NotRegisterClientException, IncorrectPasswordException

router = APIRouter(prefix="/clients",
                   tags=["Регистарация & Auth клиентов"])


@router.post("/register")
async def register(client_data: SClientRegister):
    client = await ClientsDAO.find_client(email=client_data.email)
    if client:
        raise ClientAlreadyExistsException
    hashed_password = get_password_hash(client_data.password)
    await ClientsDAO.add(first_name=client_data.first_name,
                                last_name=client_data.last_name,
                                phone_number=client_data.phone_number,
                                email=client_data.email,
                                hashed_password=hashed_password)
    return "You succesfully register!"


@router.post("/login")
async def login(response: Response, client_data: SClientLogin):
    client = await ClientsDAO.find_client(email=client_data.email)
    if not client:
        raise NotRegisterClientException
    password_valid = verify_password(client_data.password, client.hashed_password)
    if not password_valid:
        raise IncorrectPasswordException
    access_token = create_access_token({'sub': client.id})
    response.set_cookie("session_token", access_token, httponly=True)

    return "Авторизация прошла успешно!"