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

