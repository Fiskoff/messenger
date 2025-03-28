from fastapi import APIRouter
from schemes.user_create_scheme import UserCreateScheme
from services.create_user_services import check_user_date


user_router = APIRouter(tags=["Users"])

@user_router.post("/created_users/")
async def create_user(user_data: UserCreateScheme):
    result = await check_user_date(**user_data.model_dump())
    return result

