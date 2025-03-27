from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.env_data import env_helper


engine = create_async_engine(
    url=env_helper.DB_URL,
    echo=True
)

session_factory = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        autocommit=False,
)