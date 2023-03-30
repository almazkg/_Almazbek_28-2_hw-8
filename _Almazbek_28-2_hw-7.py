import sqlite3


def create_connection(hw_db):
    connection = None
    try:
        connection = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, products):
    try:
        cursor = connection.cursor()
        cursor.execute(products)
    except sqlite3.Error as e:
        print(e)


def create_product(connection, products):
    try:
        sql = '''INSERT INTO students 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(connection, products):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products1(connection, products):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price_limit(connection, limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? and quantity >?'''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_products(connection):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE '%Мыло%' '''
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


data_base_products = 'pythonProject3'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(8,2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0)
'''

db_connection = create_connection(data_base_products)
if db_connection is not None:
    print('Connected successfully!')
    # create_table(db_connection, sql_create_products_table)
    # create_product(db_connection,("Жидкое мыло", 230.0, 500))
    # create_product(db_connection, ("Полотенца бумажные", 77.12, 100))
    # create_product(db_connection, ("Бумага туалетная", 11.22, 800))
    # create_product(db_connection, ("Тряпка для мытья пола", 99.3, 50))
    # create_product(db_connection, ("Одноразовые стаканы", 7.0, 1000))
    # create_product(db_connection, ("Мешки для мусора", 4.2, 1340))git
    # create_product(db_connection, ("Хозяйственное мыло", 41.82, 300))
    # create_product(db_connection, ("Одноразовые тарелки", 7.0, 1000))
    # create_product(db_connection, ("Ведро-контейнер для мусора с педалью", 1500.0, 12))
    # create_product(db_connection, ("Перчатки хозяйственные латексные", 77.09, 400))
    # create_product(db_connection, ("Вешалки-плечики", 93.0, 70))
    # create_product(db_connection, ("Салфетки влажные", 25.55, 600))
    # create_product(db_connection, ("Салфетки", 14.12, 700))
    # create_product(db_connection, ("Крем для рук", 123.12, 150))
    # create_product(db_connection, ("Крем для лица", 360.12, 150))

    # update_products(db_connection, (33, 15))
    # update_products1(db_connection, (13.14, 3))
    # delete_products(db_connection, 3)
    # select_all_products(db_connection)
    # select_products_by_price_limit(db_connection, (100, 5))
    # search_products(db_connection)

    db_connection.close()
    print('DONE!')
