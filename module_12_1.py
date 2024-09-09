import unittest

class Runner:
    def __init__(self, name='Test'):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rnd = Runner()
        for _ in range(10):
            rnd.walk()
        self.assertEqual(rnd.distance, 50)

    def test_run(self):
        rnd = Runner()
        for _ in range(10):
            rnd.run()
        self.assertEqual(rnd.distance, 100)

    def test_challenge(self):
        rnd = Runner()
        rnd1 = Runner()
        for _ in range(10):
            rnd.run()
            rnd1.walk()
        self.assertNotEqual(rnd.distance, rnd1.distance)


if __name__ == '__main__':
    unittest.main()