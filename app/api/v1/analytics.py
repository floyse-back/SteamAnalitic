from fastapi import APIRouter,Depends
from app.infrastructure.db.database import get_async_db
from app.utils.dependencies import user_auth_check
from app.application.steam_analitic.analitic_use_cases import AnaliticService

router = APIRouter(prefix="/api/v1/analytics")

analitic_service = AnaliticService()


@router.get("/user_battle",response_model=None)
async def analytics(user1_id:str, user2_id:str, auth = Depends(user_auth_check)):
    return await analitic_service.analitic_user_battle(user1_id,user2_id)

@router.get("/user_score/")
async def user_score_generate(user:str, auth = Depends(user_auth_check)):
    return {
        "user_rating": await analitic_service.analitic_user_rating(user)
    }

@router.get("/friends_list/")
async def friend_game_list(user:str, auth = Depends(user_auth_check)):
    return await analitic_service.friends_game_list(user)

@router.get("/games_for_you")
async def games_for_you(user:str,session = Depends(get_async_db), auth = Depends(user_auth_check)):
    return await analitic_service.analitic_games_for_you(user,session = session)

@router.get("/salling_for_you")
async def salling_for_games_you(user:str,auth = Depends(user_auth_check),session = Depends(get_async_db)):
    return await analitic_service.salling_for_you_games(user=user,session=session)

@router.get("/user_achivements/")
async def user_achivements(steam_id:str, app_id:int, auth = Depends(user_auth_check)):
    return await analitic_service.user_achivements(steam_id,app_id)


