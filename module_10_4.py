from queue import Queue
from threading import Thread
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
        sleep(rd(3,10))


class Cafe:
    def __init__(self, *args):
        self.queue = Queue
        for i in args:
            self.table = Table(i)


    def guest_arrival(self, *guests):
        for i in guests:
            if  self.table.guest == None:
                self.table.guest = i
                tabl_guest = Thread(target = Guest, args = (i,))
                tabl_guest.start()
                print(f'{i} сел(а) за стол номер {self.table.number}')
            else:
                self.queue.put()
                print(f'{i} в очереди')

    def  discuss_guests(self):
        if queue.empty() or self.table.guest != None:
            if self.table.guest != None and Guest.is_alive() == False:
                print(f'{self.guest} покушал(а) и ушел(ла)')
                print(f'Стол номер {self.number} свободен')
                self.table.guest = None
            elif queue.empty() and self.table.guest == None:
                self.table.guest = self.queue.get()
                print(f'{self.table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {self.number}')
                tabl_guest = Thread(target=Guest, args=(self.table.guest,))
                tabl_guest.start()


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







