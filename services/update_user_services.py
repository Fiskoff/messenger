from repository.update_user import update_password, update_value
from repository.check_user_data import check_old_password, check_field_uniqueness


async def update_password_service(user_id: int, old_password: str, new_password: str) -> dict:
    try:
        await check_old_password(user_id, old_password)
        await update_password(user_id, new_password)
        return {"status": "success", "message": "Пароль успешно изменён"}
    except ValueError as error:
        return {"status": "error", "message": str(error)}


async def validate_unique_field(field_name: str, value: str) -> bool | str:
    try:
        await check_field_uniqueness(field_name, value)
        return True
    except ValueError as error:
        return f"{error}"


async def update_user_value(field_name: str, value: str, id_user: int) -> dict:
    message_check = await validate_unique_field(field_name, value)
    if  message_check is True:
        message_update = await update_value(field_name, value, id_user)
        if message_update is True:
            return {"status": "success", "message": f"Значение {value} сохранено"}
        else:
            print(f"Ошибка обновления: {message_update}")
            return {"status": "error", "message": message_update}
    else:
        print(f"Ошибка проверки уникальности: {message_check}")
        return {"status": "error", "message": message_check}