from pydantic import BaseModel, constr


class UpdateNicknameScheme(BaseModel):
    user_id: int
    new_nickname: constr(min_length=3, max_length=50, strip_whitespace=True)

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "new_nickname": "New Sergey",
            }
        }
