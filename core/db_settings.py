from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.env_data import env_helper


class DataBaseSettings:
    def __init__(self):
        self.engine = create_async_engine(
            url = env_helper.DB_URL,
            echo = True
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db_settings = DataBaseSettings()
