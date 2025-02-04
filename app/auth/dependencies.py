from fastapi import Request, Depends
from app.clients.dao import ClientsDAO
from app.exceptions import NotTokenException, IncorrectTokenFormatException, TokenExpiredException, \
    NotRegisterClientException, NotRegisterMasterException, MasterRegisterException
from jose import jwt, JWTError
from app.database import settings
from datetime import datetime

from app.masters.dao import MastersDAO


async def get_token(request: Request):
    token = request.cookies.get("session_token")
    if not token:
        raise NotTokenException
    return token


async def get_masters_token(request: Request):
    token = request.cookies.get("masters_token")
    if not token:
        raise MasterRegisterException
    return token


async def get_current_client(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get('exp')
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException
    client_id: int = payload.get('sub')
    if not client_id:
        raise NotRegisterClientException
    client = await ClientsDAO.find_one(id=int(client_id))
    if not client:
        raise NotRegisterClientException
    return client


async def get_current_master(token: str = Depends(get_masters_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get('exp')
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException
    masters_id: int = payload.get('sub')
    if not masters_id:
        raise NotRegisterMasterException
    master = await MastersDAO.find_one(id=int(masters_id))
    if not master:
        raise NotRegisterMasterException
    return master
