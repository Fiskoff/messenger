from os import getenv
from dotenv import load_dotenv


class EnvData:
    load_dotenv()

    DB_URL = getenv("DB_URL")

    SERVER_HOST = getenv("SERVER_HOST")
    SERVER_PORT = int(getenv("SERVER_PORT"))


env_helper = EnvData
