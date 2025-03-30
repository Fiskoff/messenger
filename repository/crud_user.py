from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel


async def create_user(**user_data):
    new_user = UserModel(
        nickname=user_data["nickname"],
        email_address=user_data["email_address"],
        phone_number=user_data["phone_number"],
        password=user_data["password"]
    )

    async with db_settings.session_factory() as session:
        session.add(new_user)
        await session.commit()


async def get_user_id(nickname=None) -> int | None:
    stmt = select(UserModel.id).where(UserModel.nickname == nickname)

    async with db_settings.session_factory() as session:
        user_id = await session.execute(stmt)
        return user_id.scalars().first()



async def delete_user(user_id: int) -> UserModel | None:
    stmt = select(UserModel).where(UserModel.id == user_id)

    async with db_settings.session_factory() as session:
        result = await session.execute(stmt)
        user = result.scalars().first()

        if user:
            await session.delete(user)
            await session.commit()
            return user
        return None