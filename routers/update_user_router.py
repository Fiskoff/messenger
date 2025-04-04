from fastapi import APIRouter, Query
from enum import Enum
from pydantic import Field
from typing import Annotated

from services.update_user_services import update_user_value, update_password_service
from schemes.update_user_scheme import FieldName

update_user = APIRouter(tags=["Users/update"])


@update_user.put("/password/")
async def update_user_password(user_id: int, old_password: str, new_password: str) -> dict:
    return await update_password_service(user_id=user_id, old_password=old_password, new_password=new_password)


@update_user.put("/update/")
async def update_values(
    field_name: Annotated[FieldName, Query(title="Field Name", description="Выберите поле для обновления", example="nickname")],
    value: Annotated[str, Query(title="New Value", description="Новое значение для выбранного поля")],
    user_id: Annotated[int, Query(title="User ID", description="ID пользователя для обновления")]
) -> dict:
    return await update_user_value(field_name, value, user_id)