from repository.update_user import update_nickname, update_email, update_phone, update_password
from repository.check_user_data import check_old_password


async def update_nickname_service(user_id: int, new_nickname: str) -> dict:
    result = await update_nickname(user_id=user_id, new_nickname=new_nickname)

    if result:
        return {"status": "success", "message": "Никнейм изменён"}
    else:
        return {"status": "error", "message": "Никнейм изменить не удалось"}


async def update_email_service(user_id: int, new_email: str) -> dict:
    result = await update_email(user_id=user_id, new_email=new_email)

    if type(result) is bool:
        return {"status": "success", "message": "Адрес электронной почты изменён"}
    else:
        return {"status": "error", "message": f"{result}"}


async def update_phone_service(user_id: int, new_phone: str) -> dict:
    result = await update_phone(user_id=user_id, new_phone=new_phone)

    if type(result) is bool:
        return {"status": "success", "message": "Номер телефона изменён"}
    else:
        return {"status": "error", "message": f"{result}"}


async def update_password_service(user_id: int, old_password: str, new_password: str) -> dict:
    try:
        await check_old_password(user_id, old_password)
        await update_password(user_id, new_password)
        return {"status": "success", "message": "Пароль успешно изменён"}
    except ValueError as error:
        return {"status": "error", "message": str(error)}