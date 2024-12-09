import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()
# Функция для инициализации базы данных и создания таблицы Products
def initiate_db(db_name="database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
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

connection.commit()
connection.close()
