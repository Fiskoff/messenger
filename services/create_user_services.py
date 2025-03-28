import asyncio
from repository.create_user_repository import create_user
from repository.check_user_date import CheckUniquenessData
from services.password_hashing import hashing_user_password


async def check_user_date(**user_data: dict) -> dict:
    checker = CheckUniquenessData(
        nickname=user_data["nickname"],
        email_address=user_data["email_address"],
        phone_number=user_data["phone_number"],
        password=user_data["password"]
    )

    basic_check = await checker.check_all_exists()
    if not basic_check[0]:
        return {"status": "error", "message": f' Уже используется: "{basic_check[1]}"'}

    password_check = await checker.check_password_exists()
    if not password_check[0]:
        return {"status": "error", "message": f' Уже используется: "{password_check[1]}"'}

    # Хеширование и создание пользователя
    try:
        hashed_password = hashing_user_password(user_data["password"])
        user_data["password"] = hashed_password
        await create_user(**user_data)
        return {"status": "success", "message": "Пользователь создан"}
    except Exception as error:
        return {"status": "error", "message": f"Ошибка создания: {str(error)}"}

"""
async def main():
    result = await check_user_date(
        nickname="S34",
        email_address="s34",
        phone_number="+34",
        password="123456"
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
"""