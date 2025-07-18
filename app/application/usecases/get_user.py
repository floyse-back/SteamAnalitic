from app.application.dto.user_dto import UserModelDTO
from app.application.exceptions.exception_handler import UserNotFound
from app.domain.logger import ILogger
from app.domain.users.repository import IUserRepository

class GetUserUseCase:
    def __init__(self,user_repository:IUserRepository,logger:ILogger):
        self.user_repository = user_repository
        self.logger = logger

    async def execute(self,session,user_id:int|None = None,email: str|None = None,username:str|None = None)->UserModelDTO:
        if user_id != None:
            user_model = await self.user_repository.get_user_for_id(session = session,user_id=user_id)
        elif email != None:
            user_model = await self.user_repository.get_user_for_email(session = session,email=email)
        elif username != None:
            user_model = await self.user_repository.get_user(session = session,username = username)
        else:
            raise UserNotFound

        if user_model == None:
            raise UserNotFound

        self.logger.info(f"User {user_model.id} is getting a user")

        return user_model