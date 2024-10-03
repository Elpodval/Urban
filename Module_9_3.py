# -*- coding: utf-8 -*-

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для first_result с zip
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для second_result без zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))