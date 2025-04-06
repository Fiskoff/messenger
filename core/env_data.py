from os import getenv
from dotenv import load_dotenv


class EnvData:
    load_dotenv()

    DB_URL = getenv("DB_URL")

    SERVER_HOST = getenv("SERVER_HOST")
    SERVER_PORT = int(getenv("SERVER_PORT"))

    SECRET_KEY = getenv("SECRET_KEY")
    ALGORITHM = getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


env_helper = EnvData
