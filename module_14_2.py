import sqlite3
from distutils.util import execute

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()


cursor.execute('DELETE FROM Users WHERE id = ?',(6,))
cursor.execute('SELECT SUM(balance) FROM Users')
sum_ = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM Users')
count_ = cursor.fetchone()[0]
print(f'Сумма всех балансов: {sum_}')
print(f'Количество пользователей: {count_}')
print(f'Средний баланс для одного пользователя: {sum_/count_}')

connection.commit()
connection.close()