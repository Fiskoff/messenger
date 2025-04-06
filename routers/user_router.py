from fastapi import APIRouter

from models.user_model import UserModel
from schemes.user_scheme import UserCreateScheme
from services.user_services import create_user_services, get_user_id_services, delete_user_services, get_user_services, get_user_by_login_service


user_router = APIRouter(tags=["Users"])


@user_router.post("/created_user/")
async def create_user(user_data: UserCreateScheme) -> dict:
    return await create_user_services(**user_data.model_dump())


@user_router.get("/get_id_user/")
async def get_user_id(user_login: str) -> int | dict:
    return await get_user_id_services(login=user_login)


@user_router.delete("/delete_user/")
async def delete_user(user_id: int) -> dict:
    return await delete_user_services(user_id=user_id)

@user_router.get("/get_user/")
async def get_user(user_id: int) -> dict:
    return await get_user_services(user_id=user_id)


@user_router.get("/get_user_by_login")
async def get_user_by_login_(login: str) -> dict:
    user_dict = await get_user_by_login_service(login)
    del user_dict["password"]
    return user_dict