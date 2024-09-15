from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли к администратору'

@app.get('/user/{user_id}')
async def welcome_user(user_id) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def welcome_id_user(username: str = 'Unknow', age: int = 0) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст {age}'

# python -m uvicorn module_15_1:app - запуск сервера