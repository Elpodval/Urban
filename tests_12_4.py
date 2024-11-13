import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',  # Параметр filemode должен быть 'w', чтобы файл перезаписывался
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


def skip_if_frozen(test_func):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(123, speed=10)  # Передаём число вместо строки
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("Usain", speed=-5)  # Передаём отрицательное значение скорости
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        usain = Runner("Usain", speed=10)
        nik = Runner("Nik", speed=3)
        tournament = Tournament(90, usain, nik)
        results = tournament.start()
        self.assertEqual(results[1].name, "Usain")

    @skip_if_frozen
    def test_second_tournament(self):
        andrei = Runner("Andrei", speed=9)
        nik = Runner("Nik", speed=3)
        tournament = Tournament(90, andrei, nik)
        results = tournament.start()
        self.assertEqual(results[1].name, "Andrei")

    @skip_if_frozen
    def test_third_tournament(self):
        usain = Runner("Usain", speed=10)
        andrei = Runner("Andrei", speed=9)
        nik = Runner("Nik", speed=3)
        tournament = Tournament(90, usain, andrei, nik)
        results = tournament.start()
        self.assertEqual(results[1].name, "Andrei")


if __name__ == "__main__":
    # Запускаем тесты
    unittest.main()
