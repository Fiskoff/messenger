from fastapi import FastAPI
from uvicorn import run

from core.env_data import env_helper
from routers.user_router import user_router


app = FastAPI()
app.include_router(user_router, prefix="/api")


if __name__ == '__main__':
    run(app, host=env_helper.SERVER_HOST, port=env_helper.SERVER_PORT)

