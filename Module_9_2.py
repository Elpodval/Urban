# -*- coding: utf-8 -*-

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


# Сборка для first_result: длины строк не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Сборка для second_result: пары слов одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Сборка для third_result: словарь из строк и их длин, только с чётной длиной
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)