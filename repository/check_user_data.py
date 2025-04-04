from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel
from services.password_hashing import verify_password


class CheckUniquenessData:
    def __init__(self, login: str, nickname: str, email_address: str, phone_number: str):
        self.login = login
        self.nickname = nickname
        self.email_address = email_address
        self.phone_number = phone_number


    async def check_all_exists(self) -> bool:
        checks = [
            (UserModel.login, self.login),
            (UserModel.email_address, self.email_address),
            (UserModel.phone_number, self.phone_number)
        ]
        async with db_settings.session_factory() as session:
            for column, value in checks:
                stmt = select(UserModel).where(column == value)
                if (await session.execute(stmt)).scalars().first():
                    return False
            return True


async def check_old_password(user_id: int, old_password: str) -> bool:
    async with db_settings.session_factory() as session:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await session.execute(stmt)
        user = result.scalars().first()

        if user is None:
            raise ValueError("Пользователь не найден")

        if not verify_password(old_password, user.password):
            raise ValueError("Старый пароль неверен")

        return True


async def check_field_uniqueness(fild_name: str, value: str) -> bool:
    if fild_name == "nickname":
        return True
    else:
        fild = getattr(UserModel, fild_name)
        async with db_settings.session_factory() as session:
            stmt = select(UserModel).where(fild == value)
            if (await session.execute(stmt)).scalars().first():
                raise ValueError(f"Значение {value} занято")
            return True
