# -*- coding: utf-8 -*-


import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаем содержимое файла и обрабатываем его
                content = file.read().lower()  # Приводим к нижнему регистру
                # Убираем пунктуацию
                content = content.translate(str.maketrans('', '', string.punctuation + ' -'))
                # Разбиваем строку на слова
                words = content.split()
                all_words[file_name] = words  # Сохраняем слова в словарь
        return all_words

    def find(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Позиция слова (считаем с 1)
                result[file_name] = position
        return result

    def count(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений слова
            if count > 0:
                result[file_name] = count
        return result

# Пример использования класса
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # Позиция слова по счёту
print(finder.count('teXT'))  # Количество слов в тексте всего