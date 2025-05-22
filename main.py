from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
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
