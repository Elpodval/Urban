import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем объект TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создаем объект TextTestRunner и запускаем тесты
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)