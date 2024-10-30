import requests

url = "https://www.example.com"

response = requests.get(url)  # Функция get() для отправки GET-запроса

response.raise_for_status() # Проверка на ошибки (HTTP 200 OK)

print(f"Статус код: {response.status_code}") # Получение кода статуса ответа

print(f"Заголовки ответа:\n{response.headers}") #Получение заголовков

print(f"Текст ответа:\n{response.text[:500]}") # Вывод первых 500 символов текста ответа (ограничение для краткости)

# Дополнительный пример с POST запросом:
data = {'key1': 'value1', 'key2': 'value2'}
post_response = requests.post(url, data=data)
print(f"POST запрос: {post_response.status_code}")

#Демонстрируемые функции/методы: get(), raise_for_status(), status_code, headers, text.
#requests существенно упрощает взаимодействие с веб-сервисами, предоставляя интуитивный
# и эффективный способ отправки различных HTTP-запросов и обработки ответов.
#Это значительно расширяет возможности Python в области веб-скрапинга, автоматизации и интеграции с внешними API.
#----------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# Создаем DataFrame из словаря
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

print("Исходный DataFrame:\n", df)  # Вывод DataFrame

# Вычисляем среднее значение столбца 'col1'
mean_col1 = df['col1'].mean()
print(f"\nСреднее значение col1: {mean_col1}") #Использование метода mean()

# Добавляем новый столбец, который является результатом операции с другими столбцами
df['col4'] = df['col1'] * df['col2'] + df['col3']
print(f"\nDataFrame с новым столбцом:\n", df) # Добавление столбца

# Фильтрация данных
filtered_df = df[df['col4'] > 10]
print(f"\nОтфильтрованный DataFrame:\n", filtered_df)  # Фильтрация данных


#Пример загрузки данных из CSV файла
try:
    csv_data = pd.read_csv("data.csv") # Чтение из файла
    print(f"\nДанные из CSV:\n{csv_data.head()}") # вывод первых строк
except FileNotFoundError:
    print("Файл data.csv не найден.")


#Демонстрируемые функции/методы: DataFrame(), mean(), индексирование столбцов,
# булево индексирование (df[df['col4'] > 10]), read_csv().
#pandas предоставляет мощные инструменты для работы с данными, включая обработку, анализ и манипулирование данными,
# значительно повышая эффективность работы с таблицами и большими наборами данных в Python.
#----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графика
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем линейный график
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("График функции sin(x)")
plt.grid(True) #добавление сетки
plt.show()


# Гистограмма
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Гистограмма')
plt.show()

#Точечный график (scatter plot)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = (30 * np.random.rand(50))**2
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.title('Точечный график')
plt.show()

#Демонстрируемые функции/методы: plot(), xlabel(), ylabel(), title(), grid(), hist(), scatter(), show().
# matplotlib — фундаментальная библиотека для визуализации данных в Python. 
#Она позволяет создавать различные типы графиков, диаграмм и визуализаций, что делает анализ данных намного нагляднее и понятнее.
#Это значительно расширяет возможности Python в области анализа данных и представления результатов.
