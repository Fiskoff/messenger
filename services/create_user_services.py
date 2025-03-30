from repository.create_user_repository import create_user
from repository.check_user_data import CheckUniquenessData
from services.password_hashing import hashing_password


async def check_user_date(**user_data: dict) -> dict:
    checker = CheckUniquenessData(
        nickname=user_data["nickname"],
        email_address=user_data["email_address"],
        phone_number=user_data["phone_number"],
    )

    input_data_check = await checker.check_all_exists()
    if not input_data_check[0]:
        return {"status": "error", "message": f' Уже используется: "{input_data_check[1]}"'}

    try:
        user_data["password"] = hashing_password(user_data["password"])
        await create_user(**user_data)
        return {"status": "success", "message": "Пользователь создан"}
    except Exception as error:
        return {"status": "error", "message": f"Ошибка создания: {str(error)}"}
