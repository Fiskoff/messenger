from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel
from services.password_hashing import hashing_password


async def update_password(user_id: int, new_password: str) -> bool:
    async with db_settings.session_factory() as session:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await session.execute(stmt)
        user = result.scalars().first()
        if user is None:
            raise ValueError("Пользователь не найден")
        user.password = hashing_password(new_password)
        session.add(user)
        await session.commit()
        return True


async def update_value(fild_name: str, new_value: str, user_id: int) -> bool | str:
    stmt = select(UserModel).where(UserModel.id == user_id)
    try:
        async with db_settings.session_factory() as session:
            result = await session.execute(stmt)
            user = result.scalars().first()
            if user is None:
                return f"Пользователь не найден"
            setattr(user, fild_name, new_value)
            session.add(user)
            await session.commit()
            return True
    except Exception as error:
        return f"{error}"