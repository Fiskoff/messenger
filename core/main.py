from uvicorn import run
from fastapi import FastAPI

from core.env_data import env_helper


app = FastAPI()


if __name__ == '__main__':
    run(app, host=env_helper.SERVER_HOST, port=env_helper.SERVER_PORT)


