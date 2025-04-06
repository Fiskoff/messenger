from fastapi import FastAPI
from uvicorn import run

from core.env_data import env_helper
from routers.user_router import user_router
from routers.update_user_router import update_user
from routers.auth_router import auth_router


app = FastAPI()
app.include_router(user_router)
app.include_router(update_user)
app.include_router(auth_router)


if __name__ == '__main__':
    run(app, host=env_helper.SERVER_HOST, port=env_helper.SERVER_PORT)

