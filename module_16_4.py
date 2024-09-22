from fastapi import FastAPI, Path, Body
from typing import Annotated
from typing import List
from pydantic import BaseModel
from starlette.exceptions import HTTPException

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def first_welcome() -> str:
    return 'Hello World'

@app.get('/users')
async def welcome() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def welcome_id_user(username: str, age = int) -> str:
    id_name = len(users)+1
    users.append(User(id = id_name, username = username, age = age))
    return f'User {id_name} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def change_id_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f'User {user_id} has been updated'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def del_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')



# python -m uvicorn module_16_3:app - запуск сервера