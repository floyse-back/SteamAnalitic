from fastapi import APIRouter, Query, Path, HTTPException, Depends
from app.database.orm import SteamORM
from app.database.database import get_async_db
from steam_web_api import Steam
from httpx import AsyncClient
from app.config import STEAM_API_KEY, HOST
from app.services.tasks import update_or_add_game
router = APIRouter(prefix="/api/v1/steam")

steam = Steam(STEAM_API_KEY)
db = SteamORM()

@router.get("/best_sallers/")
async def best_sallers(session = Depends(get_async_db),page:int=Query(default=1,gt=0),limit:int=Query(default=100,gt=-1)):
    result = await db.get_most_discount_games(session,page,limit)
    return result

@router.get("/users_full_stats/{user_id}")
async def user_full_stats(user_id:str):
    try:
        my_int = int(user_id)
        user_data =steam.users.get_user_details(f"{my_int}")
    except Exception:
        user_data = steam.users.search_user(f"{user_id}")
        user_id = user_data["player"]["steamid"]

    try:
        user_friends_list = steam.users.get_user_friends_list(f"{user_id}")
        user_badges = steam.users.get_user_badges(f"{user_id}")
        user_games = steam.users.get_owned_games(f"{user_id}")
    except Exception:
        return HTTPException(
            status_code = 404,
            detail = f"User {user_id} not found",
            headers = {"WWW-Authenticate": "Bearer"},
        )


    data_dict = {
        "user_data":user_data,
        "user_friends_list":user_friends_list,
        "user_badges":user_badges,
        "user_games":user_games,
    }
    return data_dict

@router.get("/game_stats/{steam_id}")
async def game_stats(steam_id:int =Path(gt=-1)):
    filters ='basic,controller_support,dlc,fullgame,developers,demos,price_overview,metacritic,categories,genres,recommendations,achievements'
    result = steam.apps.get_app_details(steam_id,filters=filters)

    update_or_add_game.apply_async(args=[result,steam_id])
    return result

@router.get("/get_top_games/")
async def get_top_games(session=Depends(get_async_db),limit:int=Query(default=100,gt=-1),page:int=Query(default=1,gt=0)):
    result = await db.get_top_games(session,page,limit)

    return result

@router.get("/game_achivements")
async def game_achivements(game_id,session = Depends(get_async_db)):
    async with AsyncClient() as client:
        response = await client.get(f"https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid={game_id}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Game {game_id} not found")

    return response.json()

