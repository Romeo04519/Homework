import sqlite3

def initiate_db():
    connection = sqlite3.connect('products2.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('products2.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        connection.commit()
        connection.close()
        return True
    connection.commit()
    connection.close()
    return False


def add_user(username, email, age):
    if is_included(username) is True:
        connection = sqlite3.connect('products2.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
        connection.commit()
        connection.close()

def add_products(title, description, price):
    connection = sqlite3.connect('products2.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))
    connection.commit()
    connection.close()

def get_all_product():
    connection = sqlite3.connect('products2.db')
    cursor = connection.cursor()
    cursor.execute(('SELECT * FROM Products'))
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users
#add_products('Продукт 1', 'Уютный дом', '4000000')
# add_products('Продукт 2', 'бодрящий напиток','100')
# add_products('Продукт 3', 'поездка в горы','50000')
# add_products('Продукт 4', 'баскетбольный мяч','5000')
# initiate_db()
# print(get_all_product())

add_user('rr4r','wer@mail.ru',23)