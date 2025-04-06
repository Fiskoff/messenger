from models.user_model import UserModel
from repository.crud_user import create_user, get_user_id, delete_user, get_user, get_user_by_login
from repository.check_user_data import CheckUniquenessData
from services.password_hashing import hashing_password


async def check_user_data(**user_data: dict) -> dict:
    checker = CheckUniquenessData(
        login=user_data["login"],
        nickname=user_data["nickname"],
        email_address=user_data["email_address"],
        phone_number=user_data["phone_number"],
    )

    input_data_check = await checker.check_all_exists()
    return input_data_check


async def create_user_services(**user_data: dict) -> str:
    is_allowed = await check_user_data(**user_data)

    if is_allowed:
        try:
            user_data["password"] = hashing_password(user_data["password"])
            await create_user(**user_data)
            return {"status": "success", "message": "Пользователь создан"}
        except Exception as error:
            return {"status": "error", "message": f"Ошибка создания: {str(error)}"}
    else:
        return {"status": "error", "message": f"Одно из полей уже занято"}


async def get_user_id_services(login=None) -> int | str:
    user_id = await get_user_id(login=login)

    if user_id is None:
        return {"message": "Пользователь не найден"}
    return user_id


async def delete_user_services(user_id: int) -> dict:
    user = await delete_user(user_id=user_id)
    if user is None:
        return {"status": "error", "message": "Пользователь не найден"}
    return {"status": "success", "message": f"Пользователь id: {user.id} nickname: {user.nickname} удалён"}


async def get_user_services(user_id: int) -> dict:
    user = await get_user(user_id)

    if user is None:
        return {"status": "error", "message": "Пользователь не найден"}
    return {
        "status": "success",
        "message": f"Пользователь id: {user.id}",
        "login": user.login,
        "nickname": user.nickname,
        "phone_number": user.phone_number,
        "email_address": user.email_address
    }

async def get_user_by_login_service(login: str) -> dict:
    user = await get_user_by_login(login)
    if user:
        user_dict = user.__dict__
        del user_dict["_sa_instance_state"]
        return user_dict
    else:
        return {"status": "error", "message": "Пользователь не найден"}
