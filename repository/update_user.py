import asyncio
from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel
from repository.check_user_data import check_email_address, check_phone_number
from services.password_hashing import hashing_password


async def update_nickname(user_id: int, new_nickname: str) -> bool:
    stmt = select(UserModel).where(UserModel.id == user_id)

    async with db_settings.session_factory() as session:
        result = await session.execute(stmt)
        user = result.scalars().first()
        user.nickname = new_nickname
        session.add(user)
        await session.commit()
        return True


async def update_email(user_id: int, new_email: str) -> bool | str:
    stmt = select(UserModel).where(UserModel.id == user_id)

    try:
        await check_email_address(new_email)
        async with db_settings.session_factory() as session:
            result = await session.execute(stmt)
            user = result.scalars().first()
            user.email_address = new_email
            session.add(user)
            await session.commit()
            return True
    except ValueError as error:
        return f"{error}"


async def update_phone(user_id: int, new_phone) -> bool | str:
    stmt = select(UserModel).where(UserModel.id == user_id)

    try:
        await check_phone_number(new_phone)
        async with db_settings.session_factory() as session:
            result = await session.execute(stmt)
            user = result.scalars().first()
            user.phone_number = new_phone
            session.add(user)
            await session.commit()
            return True
    except ValueError as error:
        return f"{error}"


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

