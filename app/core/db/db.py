import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo_pool=True)


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(),
        onupdate=datetime.now(),
    )


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def drop_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session
