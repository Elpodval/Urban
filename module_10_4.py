import random
import time
import threading
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом, по умолчанию None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Ожидание от 3 до 10 секунд
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверяем наличие свободных столов
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # Садим гостя за стол
                    guest.start()  # Запускаем поток
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если свободных столов нет
                self.queue.put(guest)  # Ставим в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Обслуживаем гостей, пока очередь не пуста или хотя бы один стол занят
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  # Проверяем очередь
                        next_guest = self.queue.get()  # Берем следующего гостя из очереди
                        table.guest = next_guest
                        next_guest.start()  # Запускаем поток
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Мария', 'Олег', 'Вахтанг', 'Сергей', 'Дарья', 'Арман',
        'Виктория', 'Никита', 'Галина', 'Павел', 'Илья', 'Александра'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()