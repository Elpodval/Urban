import sqlite3
import random, string

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#Добавляем данные в БД, закомментировано чтобы не плодить однотипные данные:
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                    (f"newuser{i}", f"{i}ex@outlook.com", str(random.randint(18, 65)), 1000))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой 3ей записи начиная с 1ой
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Вывод результатов в консоль
for username, email, age, balance in results:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()