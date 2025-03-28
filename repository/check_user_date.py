import asyncio
from sqlalchemy import select

from core.db_settings import db_settings
from models.user_model import UserModel


class CheckUniquenessData:
    def __init__(self, nickname: str, email_address: str, phone_number: str):
        self.nickname = nickname
        self.email_address = email_address
        self.phone_number = phone_number

    async def check_all_exists(self) -> bool | tuple:
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


"""
async def main():
    checker = CheckUniquenessData(
        nickname="Sergey",
        email_address="sergey@example.com",
        phone_number="+123456789"
    )
    result = await checker.check_all_exists()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
"""