from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

class User(BaseModel):
    username: str
    age: int

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"


"""Объяснение кода:
Импорт библиотек: Используются FastAPI для создания приложения и HTTPException для обработки ошибок.
Словарь пользователей: Изначально содержит одного пользователя.
Модель пользователя: Используется для валидации входящих данных.
GET запрос: Возвращает текущий словарь пользователей.
POST запрос: Добавляет нового пользователя с максимальным ID.
PUT запрос: Обновляет информацию о пользователе по ID.
DELETE запрос: Удаляет пользователя по ID.
Примеры запросов:
GET /users: Возвращает текущий словарь пользователей.
POST /user/UrbanUser/24: Добавляет нового пользователя и возвращает сообщение о регистрации.
POST /user/NewUser/22: Добавляет еще одного пользователя.
PUT /user/1/UrbanProfi/28: Обновляет информацию о пользователе с ID 1.
DELETE /user/2: Удаляет пользователя с ID 2.
GET /users: Возвращает обновленный словарь пользователей."""