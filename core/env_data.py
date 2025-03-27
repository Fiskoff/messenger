from os import getenv
from dotenv import load_dotenv


class EnvData:
    load_dotenv()

    DB_URL = getenv("DB_URL")


env_helper = EnvData
