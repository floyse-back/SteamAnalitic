from fastapi import FastAPI
from routers import analytics,steam,users
app = FastAPI()

app.include_router(users.router,prefix="/users",tags=["users"])
app.include_router(steam.router,prefix="/steam",tags=["steam"])
app.include_router(analytics.router,prefix="/analytics",tags=["analytics"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
