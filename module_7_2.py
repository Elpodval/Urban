# -*- coding: utf-8 -*-
def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущее положение указателя файла
            start_byte = file.tell()
            # Записываем строку в файл и добавляем символ новой строки
            file.write(string + '\n')
            # Сохраняем информацию о строке
            strings_positions[(index + 1, start_byte)] = string

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)