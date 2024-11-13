import unittest
import logging

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
            runner = Runner(123, speed=-10)  # Передаём число вместо строки
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info('"test_run" выполнен успешно')

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("Usain", speed=-5)
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info('"test_walk" выполнен успешно')


if __name__ == "__main__":
    unittest.main()
