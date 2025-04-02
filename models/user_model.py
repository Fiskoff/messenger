from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.orm_settings import Base


class UserModel(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(String(32), nullable=False, unique=True, index=True)
    nickname: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    email_address: Mapped[str] = mapped_column(String(256), nullable=False, unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(String(15), nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    registration_date: Mapped[datetime] = mapped_column(server_default=func.current_timestamp(), nullable=False)
