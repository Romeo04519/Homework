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

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'не прошел проверку')
    def test_walk(self):
        try:
            rnd = Runner('Pit',-10)
            logging.info(f'"test_walk" выполнен успешно')
            for _ in range(10):
               rnd.walk()
        except:
            logging.warning(f'Неверная скорость для Runner')
        #self.assertEqual(rnd.distance, 50)

    @unittest.skipIf(is_frozen, 'не прошел проверку')
    def test_run(self):
        try:
            rnd = Runner(1 ,10)
            logging.info(f'"test_run" выполнен успешно')
            for _ in range(10):
                rnd.run()
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')

        #self.assertEqual(rnd.distance, 100)
    #
    # @unittest.skipIf(is_frozen, 'не прошел проверку')
    # def test_challenge(self):
    #     rnd = Runner('Pit',10)
    #     rnd1 = Runner('Ron',10)
    #     for _ in range(10):
    #         rnd.run()
    #         rnd1.walk()
    #     self.assertNotEqual(rnd.distance, rnd1.distance)

logging.basicConfig(level=logging.INFO, filemode='a', encoding='utf-8', filename='runner_test.log',
                        format = '%(asctime)s | %(levelname)s | %(message)s')
# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())