from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.run(power)




    def run(self, power):
        battle= 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while battle > 0:
            battle -= power
            sleep(1)
            day += 1
            print(f'{self.name} сражается {day}, осталось {battle} войнов')

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')



thr_first = Thread(target = Knight, args = ('Sir Lancelot', 10))
thr_second = Thread(target = Knight, args = ("Sir Galahad", 20))
thr_first.start()
thr_second.start()
thr_first.join()
thr_second.join()
print('Все, битвы закончились!')