from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.user_services import create_user_services
from services.auth_services import login_service
from services.auth_services import get_current_user


auth_router = APIRouter(tags=["Users/auth"])


@auth_router.post("/registration")
async def registration_user(login: str, nickname: str, email_address: str, phone_number: str, password: str) -> dict:
    return await create_user_services(
        login=login, nickname=nickname, email_address=email_address, phone_number=phone_number, password=password
    )

@auth_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_service(form_data)


@auth_router.get("/me")
async def read_users_me(current_user: str = Depends(get_current_user)) -> dict:
    return {"status": "success", "nickname": current_user}