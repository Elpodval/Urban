def all_variants(text):
    length = len(text)

    # Генерируем все подпоследовательности
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]  # Возвращаем подпоследовательность


a = all_variants("Hello")
for i in a:
    print(i)