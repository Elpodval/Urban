# -*- coding: utf-8 -*-
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Пытаемся добавить элемент к сумме
        except TypeError:
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных
            print(f'Некорректный тип данных для подсчёта суммы - {item}')  # Выводим сообщение об ошибке

    return result, incorrect_data  # Возвращаем кортеж

def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError  # Генерируем исключение, если это не коллекция

        total_sum, incorrect_data = personal_sum(numbers)  # Получаем сумму и количество некорректных данных

        # Возвращаем среднее арифметическое, обрабатываем ZeroDivisionError
        return total_sum / (len(numbers) - incorrect_data) if (len(numbers) - incorrect_data) > 0 else 0

    except ZeroDivisionError:
        return 0  # Возвращаем 0, если деление на 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None  # Возвращаем None в случае некорректного типа данных

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Список с некорректными типами
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректная коллекция