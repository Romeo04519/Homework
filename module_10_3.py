from random import randint as rd
from time import sleep
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(1,101):
            if self.balance >= 500 and self.lock.locked(): # true если закрыт
                self.lock.release()
            rand_num = rd(50,500)
            self.balance += rand_num
            print(f'Пополнение {rand_num}. Баланс:{self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(1,101):
            rand_num = rd(50,500)
            print(f'Запрос на {rand_num}')
            if rand_num <= self.balance:
                self.balance -= rand_num
                print(f'Снятие: {rand_num}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                sleep(0.001)
                self.lock.acquire()




bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')