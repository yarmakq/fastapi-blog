from abc import ABC

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.db import get_session


class BaseRepository(ABC):
    _session: AsyncSession

    def __init__(
        self,
        session: AsyncSession = Depends(get_session)
    ):
        self._session = session
