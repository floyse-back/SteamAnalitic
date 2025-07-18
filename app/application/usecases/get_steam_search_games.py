from typing import Optional

from app.application.dto.steam_dto import transform_to_dto, GameShortModel, GameListModel
from app.domain.logger import ILogger
from app.domain.steam.repository import ISteamRepository


class GetSteamSearchGamesUseCase:
    def __init__(self,steam_repository:ISteamRepository,logger:ILogger):
        self.steam_repository = steam_repository
        self.logger = logger

    async def execute(self,session,name:Optional[str],category,ganre,discount,publisher,to_price,out_price,page:int=1,limit:int=10,share=True):
        data = await self.steam_repository.search_game(session=session,page=page,limit=limit,name=name,category=category,discount=discount,publisher=publisher,ganre=ganre,to_price=to_price,out_price=out_price)
        self.logger.debug("GetSteamSearchGamesUseCase data: %s",data)

        if share:
            serialize_data = [transform_to_dto(GameShortModel,i) for i in data]
        else:
            serialize_data = [transform_to_dto(GameListModel,i) for i in data]
        return serialize_data