from app.application.dto.steam_dto import SteamUser, transform_to_dto, FriendsListModel, SteamBadgesListModel, \
    GamesList, PlayersLists
from app.application.exceptions.exception_handler import ProfilePrivate
from app.infrastructure.steam_api.client import SteamClient


class GetUserFullStatsUseCase:
    def __init__(self,steam,logger):
        self.logger = logger
        self.steam:SteamClient = steam

    async def execute(self,user,user_badges:bool = True,friends_details:bool = True,user_games:bool = True):
        user_data,user = await self.steam.get_user_info(user)
        self.logger.info("GetUserFullStatsUseCase EXECUTING, user=%s",user)
        if user_data["player"].get("communityvisibilitystate") == 3:
            user_friends_list =await self.steam.save_start_pool(self.steam.users.get_user_friends_list,raise_error=False,steam_id=user,enriched=friends_details)
            if user_friends_list is None:
                user_friends_list = {"friends":[]}
            user_badges_list =await self.steam.save_start_pool(self.steam.users.get_user_badges,func_name="user_badges",raise_error=False,steam_id=f"{user}") if user_badges else None
            user_games_list =await self.steam.save_start_pool(self.steam.users.get_owned_games,func_name="owned_games",raise_error=False,steam_id=f"{user}")  if user_games else None
            #Серіалізація даних
            self.logger.debug("User Data Information%s",user_data)
            serialize_user_data = transform_to_dto(PlayersLists, user_data,dumping=False)
            if friends_details:
                serialize_user_friends_list = transform_to_dto(FriendsListModel,user_friends_list,dumping=False)
            else:
                serialize_user_friends_list = user_friends_list
            serialize_user_badges = transform_to_dto(SteamBadgesListModel,user_badges_list,dumping=False) if user_badges and user_badges_list != {} else None
            serialize_user_games = transform_to_dto(GamesList,user_games_list,dumping=False) if user_games and user_games_list != {} else None


            return SteamUser(
                user_data = serialize_user_data,
                user_friends_list = serialize_user_friends_list,
                user_badges = serialize_user_badges,
                user_games = serialize_user_games,
            ).model_dump()
        self.logger.info("GetPlayerFullStats Profile Private %s",user)
        raise ProfilePrivate(user_profile=user_data["player"].get("personaname"))
