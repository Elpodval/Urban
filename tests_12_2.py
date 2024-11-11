import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for race_number, result in cls.all_results.items():
            formatted_result = {place: runner.name for place, runner in result.items()}
            print(f"Race {race_number}: {formatted_result}")

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrei = Runner("Andrei", speed=9)
        self.nik = Runner("Nik", speed=3)

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Nik")

    def test_race_andrei_nik(self):
        tournament = Tournament(90, self.andrei, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Nik")

    def test_race_usain_andrei_nik(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Nik")


if __name__ == "__main__":
    unittest.main()
