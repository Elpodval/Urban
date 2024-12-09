import sqlite3


# Функция для инициализации базы данных
def initiate_db(db_name='database.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')
    conn.commit()
    conn.close()


# Функция для получения всех записей из таблицы Products
def get_all_products(db_name='database.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


# Функция для добавления тестовых данных в таблицу Products
def populate_products(db_name='database.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    products = [
        ("Product1", "Минимальный витаминный комплекс", 100),
        ("Product2", "Оптимальный витаминный комплекс", 200),
        ("Product3", "Большой витаминный комплекс", 300),
        ("Product4", "Супер витаминный комплекс", 400)
    ]
    cursor.executemany('''
        INSERT INTO Products (title, description, price)
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()
    conn.close()


# Функция для добавления нового пользователя
def add_user(username, email, age, db_name='database.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))
    conn.commit()
    conn.close()


# Функция проверки, существует ли пользователь с таким именем
def is_included(username, db_name='database.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists
