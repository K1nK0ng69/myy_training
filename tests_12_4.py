import unittest
import logging
from rt_with_exceptions import Runner


logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Test Runner", speed=-5)
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(12345, speed=5)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == "__main__":
    unittest.main()
