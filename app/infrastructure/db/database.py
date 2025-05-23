from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.utils.config import ASYNC_DATABASE_URL
from sqlalchemy.ext.asyncio import async_sessionmaker


engine = create_async_engine(ASYNC_DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Депенденсі для отримання сесії
async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session

class Base(DeclarativeBase):
    pass
