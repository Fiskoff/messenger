from datetime import timedelta, datetime, timezone

from fastapi import HTTPException, status, Depends
from jwt import encode, decode, PyJWTError

from core.env_data import env_helper
from services.user_services import get_user_by_login_service
from services.password_hashing import verify_password
from schemes.auth_schemes import oauth2_scheme


async def create_access_token(payload: dict) -> str:
    access_token_expires = timedelta(minutes=env_helper.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + access_token_expires
    payload.update({"exp": expire})
    encoded_jwt = encode(payload, env_helper.SECRET_KEY, algorithm=env_helper.ALGORITHM)
    return encoded_jwt


async def login_service(form_data) -> dict:
    user_dict = await get_user_by_login_service(form_data.username)
    user_password = user_dict.get("password", None)

    if not verify_password(form_data.password, user_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = await create_access_token(payload={"sub": user_dict["nickname"]})
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось подтвердить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, env_helper.SECRET_KEY, algorithms=env_helper.ALGORITHM)
        nickname: str = payload.get("sub")
        if nickname is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    return nickname