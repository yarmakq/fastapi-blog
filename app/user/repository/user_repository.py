from sqlalchemy.ext.asyncio import AsyncSession

from app.core.repository.base_repository import (
    BaseRepository,
    Depends,
    get_session,
)


class UserRepository(BaseRepository):

    def __init__(
        self,
        session: AsyncSession = Depends(get_session)
    ):
        super().__init__(session)

    async def save(self):
        return True
