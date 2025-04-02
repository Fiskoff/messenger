from fastapi import APIRouter

from services.update_user_services import update_nickname_service, update_email_service, update_phone_service, update_password_service


update_user = APIRouter(tags=["Users/update"])


@update_user.post("/nickname/")
async def update_nickname(user_id: int, new_nickname: str) -> dict:
    return await update_nickname_service(user_id=user_id, new_nickname=new_nickname)


@update_user.post("/email/")
async def update_email(user_id: int, new_email: str) -> dict:
    return await update_email_service(user_id=user_id, new_email=new_email)


@update_user.post("/phone/")
async def update_email(user_id: int, new_phone: str) -> dict:
    return await update_phone_service(user_id=user_id, new_phone=new_phone)


@update_user.post("/password/")
async def update_user_password(user_id: int, old_password: str, new_password: str) -> dict:
    return await update_password_service(user_id=user_id, old_password=old_password, new_password=new_password)