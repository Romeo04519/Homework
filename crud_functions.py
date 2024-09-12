import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')
    connection.commit()
    connection.close()

def add_products(title, description, price):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))
    connection.commit()
    connection.close()

def get_all_product():
    connection = sqlite3.connect('products.db')
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