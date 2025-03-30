from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel
from services.password_hashing import verify_password


class CheckUniquenessData:
    def __init__(self, nickname: str, email_address: str, phone_number: str):
        self.nickname = nickname
        self.email_address = email_address
        self.phone_number = phone_number


    async def check_all_exists(self) -> tuple[bool, str]:
        checks = [
            (UserModel.nickname, self.nickname),
            (UserModel.email_address, self.email_address),
            (UserModel.phone_number, self.phone_number)
        ]
        async with db_settings.session_factory() as session:
            for column, value in checks:
                stmt = select(UserModel).where(column == value)
                if (await session.execute(stmt)).scalars().first():
                    return False, value
            return True, "success"

