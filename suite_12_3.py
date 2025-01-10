import unittest
from tests_12_3 import RunnerTest, TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(test_suite)
