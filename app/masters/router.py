from fastapi import APIRouter, Response, Depends
from app.exceptions import NotRegisterMasterException, IncorrectPasswordException, MasterAlreadyExistsException
from app.auth.auth import verify_password, create_access_token, get_password_hash
from app.masters.schemas import SMastersLogin, SMasterRegister
from app.masters.dao import MastersDAO
from app.auth.dependencies import get_current_master


router = APIRouter(prefix="/masters",
                   tags=["Auth мастеров"])


@router.post("/register")
async def register(master_data: SMasterRegister, admin=Depends(get_current_master)):
    master = await MastersDAO.find_by_phone(master_data.phone_number)
    if master:
        raise MasterAlreadyExistsException
    hashed_password = get_password_hash(master_data.password)
    await MastersDAO.add(first_name=master_data.first_name,
                         last_name=master_data.last_name,
                         phone_number=master_data.phone_number,
                         hashed_password=hashed_password,
                         rating=master_data.rating)
    return f"{admin.first_name}, you succesfully register new master!"


@router.post("/login")
async def login_masters(response: Response, master_data: SMastersLogin):
    master = await MastersDAO.find_by_phone(master_data.phone_number)
    if not master:
        raise NotRegisterMasterException
    password_valid = verify_password(master_data.password, master.hashed_password)
    if not password_valid:
        raise IncorrectPasswordException
    access_token = create_access_token({'sub': str(master.id)})
    response.set_cookie("masters_token", access_token, httponly=True)
    return "You succesfully login, master!"