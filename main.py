from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
async def hello_index():
    return {
        'message': 'Hello Index!!'
    }


@app.get('/hello')
async def hello(name: str = 'World'):
    name = name.strip().title()
    return {'message': f'Hello {name}'}


@app.post('/users')
async def create_user(user: CreateUser):
    return {
        'message': 'success',
        'email': user.email
    }


@app.get('/items')
async def list_items():
    return [
        'item1',
        'item2',
        'item3',
    ]


@app.get('/items/{item_id}')
async def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {
        'items': {
            'id': item_id,
        }
    }


@app.get('/items/latest')
async def get_latest_item():
    return {'item': {'id': '0', 'name': 'latest'}}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
