# -*- coding: utf-8 -*-
def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # Сложение чисел
        elif isinstance(a, str) and isinstance(b, str):
            return a + b  # Сложение строк
        else:
            # Если типы разные, возвращаем строковое представление
            return str(a) + str(b)
    except TypeError:  # Обработка исключения TypeError
        return str(a) + str(b)  # Возвращаем строковое представление

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))      # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456