from pydantic import BaseModel, EmailStr, constr


class UserCreateScheme(BaseModel):
    login: constr(min_length=3, max_length=50, strip_whitespace=True)
    nickname: constr(min_length=3, max_length=50, strip_whitespace=True)
    email_address: EmailStr
    phone_number: constr(min_length=11, max_length=15)
    password: constr(min_length=8, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "login": "fiskoff",
                "nickname": "Sergey",
                "email_address": "fiskoff2015@yandex.ru",
                "phone_number": "89502682589",
                "password": "password"
            }
        }


class UserGetIdScheme(BaseModel):
    login: constr(min_length=3, max_length=50, strip_whitespace=True)

    class Config:
        json_schema_extra = {
            "example": {
                "login": "fiskoff"
            }
        }