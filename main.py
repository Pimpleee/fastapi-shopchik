from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel
from core.models import Base, db_helper
from items_views import router as items_router
from users.views import router as users_router
from api import router as router_v1
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def hello_index():
    return {"message": "Hello Index!!"}


@app.get("/hello")
async def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
