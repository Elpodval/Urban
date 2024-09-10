# -*- coding: utf-8 -*-

import os
import time

print('Текущая директория:', os.getcwd())

directory = r"C:\Users\Serge\PycharmProjects\URBAN_Lessons\lessons\module_7"

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filepath = os.fsdecode(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

