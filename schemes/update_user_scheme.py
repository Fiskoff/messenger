from enum import Enum
from pydantic import BaseModel, Field


class FieldName(str, Enum):
    nickname = "nickname"
    phone_number = "phone_number"
    email_address = "email_address"

class UpdateUserRequest(BaseModel):
    field_name: FieldName = Field(..., description="Выберите поле для обновления", example=FieldName.nickname)
    value: str = Field(..., description="Новое значение для выбранного поля.")
    user_id: int = Field(..., description="ID пользователя, которого нужно обновить.")