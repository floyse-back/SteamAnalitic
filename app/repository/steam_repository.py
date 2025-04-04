from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.steam import SteamBase


class SteamRepository:
    """Репозиторій для роботи з Steam даними"""

    @staticmethod
    async def get_top_games(session:AsyncSession,page:int,limit:int):
        statement = select(SteamBase).order_by(desc(SteamBase.positive)).offset((page - 1) * limit).limit(limit)

        result = await session.execute(statement)
        return result.scalars().all()

    @staticmethod
    async def get_most_discount_games(session:AsyncSession,page:int,limit:int):
        statement = select(SteamBase).order_by(desc(SteamBase.discount)).filter(SteamBase.discount > 80).offset((page - 1) * limit).limit(limit)

        result = await session.execute(statement)
        return result.scalars().all()
