from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Создаем объект Jinja2Templates
users = []


class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/', response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users_list": users})  # Передаем request и список пользователей

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((u for u in users if u.id == user_id), None)  # Найти пользователя по ID
    if user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    return templates.TemplateResponse("users.html", {"request": request, "user": user})  # Передача данных пользователя в шаблон


# @app.get('/users')
# async def get_users() -> List[User]:
#     # Возвращаем список всех пользователей
#     return users


@app.post('/user/{username}/{age}')
async def registered_user(username: str, age: int) -> User:
    # Регистрируем нового пользователя с уникальным ID
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    # Обновляем существующего пользователя
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def deleted_user(user_id: int) -> User:
    # Удаляем пользователя по ID
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail='User was not found')