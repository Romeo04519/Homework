from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def welcome() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли к администратору'

@app.get('/user/{user_id}')
async def welcome_user(user_id: int = Path(ge=1,le=100,description='Enter User ID', example='1')) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def welcome_id_user(username: Annotated[str,Path(min_length=5,max_length=20, description= 'Enter username', example='Piter')],
                          age: int = Path(ge=18,le=120,description='Enter age', example='19')) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст {age}'

# python -m uvicorn module_15_2:app - запуск сервера