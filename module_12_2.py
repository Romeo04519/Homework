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
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant.name)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    def TearDownClass(self):
        print(self.all_result)
        # for i, k in self.all_result.items():
        #     print(f'{i}: {k} ', end = '')


    def testRun(self):
        first_check = Tournament(90, self.run_1, self.run_3)
        fin_ = first_check.start()
        self.all_result = fin_
        last_ = sorted(fin_.keys())[-1]
        word_ = str(fin_[last_])
        self.assertTrue(word_ == 'Ник')
        self.TearDownClass()


    def testRun1(self):
        first_check = Tournament(90, self.run_2, self.run_3)
        fin_ = first_check.start()
        self.all_result = {**self.all_result, **fin_}
        last_ = sorted(fin_.keys())[-1]
        self.assertTrue(fin_[last_], 'Ник')
        self.TearDownClass()


    def testRun2(self):
        first_check = Tournament(90, self.run_1, self.run_2, self.run_3)
        fin_ = first_check.start()
        self.all_result = {**self.all_result, **fin_}
        last_ = sorted(fin_.keys())[-1]
        self.assertTrue(fin_[last_], 'Ник')
        self.TearDownClass()


if __name__ == '__main__':
    unittest.main()