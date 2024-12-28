from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from typing import Annotated

# Создание экземпляра FastAPI
app = FastAPI()# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return"Главная страница"# Страница администратора

@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return"Вы вошли как администратор"# Страница пользователей с параметром в пути с валидацией
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(
    user_id: Annotated[
        int,
        Path(
            ...,
            ge=1,
            le=100,
            description="Enter User ID",            examples=1) ]):
    return f"Вы вошли как пользователь № {user_id}"# Страница пользователей с параметрами в пути
@app.get("/user/{username}/{age}", response_class=HTMLResponse)
async def read_user_info(
    username: Annotated[
        str,
        Path(
            ...,
            min_length=5,
            max_length=20,
            description="Enter username",            examples="UrbanUser"        )],    age: Annotated[
        int,
        Path(
            ...,
            ge=18,
            le=120,
            description="Enter age",            examples=24) ]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
