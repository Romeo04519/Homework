from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/')
async def first_welcome() -> str:
    return 'Hello World'

@app.get('/users')
async def welcome() -> dict:
    return users

@app.get('/user/{username}/{age}')
async def welcome_id_user(username: Annotated[str,Path(min_length=5,max_length=20, description= 'Enter username', example='Piter')],
                          age: int = Path(ge=18,le=120,description='Enter age', example='19')) -> str:
    user_id = str(int(max(users,key=int))+1)
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'User {user_id} is registered'

@app.get('/user/{user_id}/{username}/{age}')
async def change_id_user(user_id: int = Path(ge=1,le=100,description='Enter User ID', example='1')
                         , username: str = Path(min_length=5,max_length=20, description= 'Enter username', example='Piter'),
                          age: int = Path(ge=18,le=120,description='Enter age', example='19')) -> str:
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'User {user_id} has been updated'

@app.get('/user/{user_id}')
async def del_user(user_id: int = Path(ge=1,le=100,description='Enter User ID', example='1')) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'



# python -m uvicorn module_16_3:app - запуск сервера