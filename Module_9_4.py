# -*- coding: utf-8 -*-

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем map с lambda-функцией для сравнения символов
result = list(map(lambda x, y: x == y, first, second))

# Вывод результата
print(result)

#-----------------------------------------------------------------

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(f"{item}\n")  # Записываем каждое значение в файл с новой строки
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print()

#-----------------------------------------------------------------

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибуте words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из words

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())