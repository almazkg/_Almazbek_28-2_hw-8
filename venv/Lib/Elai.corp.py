import sqlite3


def create_connection(name_db):
    connection = None
    try:
        connection = sqlite3.connect(name_db)
    except sqlite3.Error as e:
        print(e)
        return connection



def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_employee(connection, employee):
    try:
        sql = '''INSERT INTO employees
        (full_name, orders, quantity)VALUES(?, ?, ?)'''
        connect = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_employees_by_quantity_limit(connection, limit):
    try:
        sql = '''SELECT * FROM employees WHERE orders >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_employee(connection, employee):
    try:
        sql = '''UPDATE employees SET orders = ?, quantity = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_employee(connection, id):
    try:
        sql = '''DELETE FROM employees WHERE id = ?'''
        cursor = connection(cursor)
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

data_base_name = 'Elai.corp.db'

sql_create_employees_table = '''
CREATE TABLE employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL,
orders DOUBLE(5,2) NOT NULL DEFAULT 0.0,
quantity TEXT DEFAULT NULL)
'''

db_connection = create_connection(data_base_name)
if db_connection is not None:
    print('connected succeccfully!')

create_table(db_connection, sql_create_employees_table)

create_employee(db_connection, ('Sam Kachiev dir.', 0.0, 0.0))
create_employee(db_connection('Aigerim Maratova', 0.0, 0.0))
create_employee(db_connection('Nurba baike', 5.0, 3000.0))
create_employee(db_connection('Chika', 8.0, 6000.0))
create_employee(db_connection('Mika', 5.0, 4000.0 ))
create_employee(db_connection('Almaz', 1.0, 480.0))

select_all_employees_by_quantity_limit()