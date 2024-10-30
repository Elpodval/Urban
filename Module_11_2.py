def introspection_info(obj):
    """Возвращает информацию о переданном объекте."""
    info = {
        'type': str(type(obj).__name__),  # Тип объекта
        'attributes': [],                  # Атрибуты объекта
        'methods': [],                     # Методы объекта
        'module': str(obj.__module__),     # Модуль, к которому принадлежит объект
    }

    # Получаем атрибуты объекта
    for attribute in dir(obj):
        if not attribute.startswith('__'):  # Игнорируем встроенные атрибуты
            if isinstance(getattr(obj, attribute), property):
                info['attributes'].append(attribute)
            else:
                info['attributes'].append(attribute)

    # Получаем методы объекта
    for method in dir(obj):
        if method.startswith('__'):  # Игнорируем встроенные методы
            continue
        if callable(getattr(obj, method)):
            info['methods'].append(method)

    return info


class SampleClass:
    """Пример класса для демонстрации интроспекции."""

    def __init__(self, name):
        self.name = name
        self.age = 0

    def greet(self):
        return f"Hello, my name is {self.name}."

    @property
    def info(self):
        return f"{self.name} is {self.age} years old."


# Создаем объект класса
sample_obj = SampleClass("Alice")

# Получаем информацию об объекте
info = introspection_info(sample_obj)
print(info)