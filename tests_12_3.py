import unittest

def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(isinstance("runner", str))

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual("walk".upper(), "WALK")

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertIn(3, [1, 2, 3])

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertNotEqual(5 - 2, 1)
