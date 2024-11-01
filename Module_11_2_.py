def introspection_info(obj):
    """Возвращает информацию о переданном объекте."""
    info = {
        'type': str(type(obj).__name__),
        'attributes': [],
        'methods': [],
        'module': None,  # Инициализируем как None
    }

    try:
        info['module'] = obj.__module__
    except AttributeError:
        pass  # Игнорируем ошибку для встроенных типов

    # Проверяем, является ли объект встроенным типом (можно упростить)
    if isinstance(obj, (int, float, str, bool, list, dict, set, tuple)):
        return info

    for attribute in dir(obj):
        if not attribute.startswith('__'):
            if isinstance(getattr(obj, attribute), property):
                info['attributes'].append(attribute)
            else:
                info['attributes'].append(attribute)

    for method in dir(obj):
        if not method.startswith('__') and callable(getattr(obj, method)):
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
info = introspection_info(sample_obj)
print(info)

number_info = introspection_info(42)
print(number_info)

sample_obj = SampleClass("Alice")

# Получаем информацию об объекте
info = introspection_info(sample_obj)
print(info)

# Пример использования с числом
number_info = introspection_info(42)
print(number_info)
