import unittest
from runner_and_tournament import Runner, Tournament


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
        runner = Runner("Usain", speed=10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Usain", speed=10)
        runner.walk()
        self.assertEqual(runner.distance, 10)

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
