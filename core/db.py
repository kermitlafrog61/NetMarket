from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from .settings import settings


engine = create_async_engine(settings.DB_ASYNC_URL, future=True)
SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
