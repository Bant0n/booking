from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session_marker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
