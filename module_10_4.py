from random import randint as rd
from time import sleep
import queue
from threading import Thread


class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(rd(3, 10)) # не срабатывает при запуске потока


class Cafe:
    tables = []
    def __init__(self, *args):
        self.queue = queue.Queue()
        for i in args:
            tabl = i.number, i.guest
            Cafe.tables.append(list(tabl))

    def guest_arrival(self, *guests_):
        for i in guests_:
            cit_ = False
            for j in Cafe.tables:
                if j[1] is None:
                    j[1] = i
                    i.start()
                    print(f'{i.name} сел(а) за стол номер {j[0]}')
                    cit_ = True
                    break
            if cit_ is False:
                self.queue.put(i)
                print(f'{i.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for j in Cafe.tables:
                if j[1].is_alive():
                    print(f'{j[1].name} покушал(а) и ушел(ла)')
                    print(f'Стол номер {j[0]} свободен')
                    j[1] = None
                if not self.queue.empty():
                    for j in Cafe.tables:
                        if j[1] is None:
                            j[1] = self.queue.get()
                            print(f'{j[1].name} вышел(-ла) из очереди и сел(-а) за стол номер {j[0]}')
                            j[1].start()







# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
