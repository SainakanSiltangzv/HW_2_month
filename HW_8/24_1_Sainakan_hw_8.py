# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов,
# поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр
# из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL)
# значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных размером 5 цифр,
# поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0

def insert_product(conn, product):
    sql = '''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

db_name = r'products_db'
create_students_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0.0
)'''

# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
def add_products(conn):
    insert_product(conn, ("beef", 100, 6))
    insert_product(conn, ("chicken", 150, 5))
    insert_product(conn, ("duck", 20, 6))
    insert_product(conn, ("lamb ", 190, 9))
    insert_product(conn, ("meat", 200, 12))
    insert_product(conn, ("mutton ", 150, 10))
    insert_product(conn, ("cod ", 85, 11))
    insert_product(conn, ("pikeperch", 65, 7))
    insert_product(conn, ("pikeperch", 598, 4))
    insert_product(conn, ("Cucumber", 120, 3))
    insert_product(conn, ("grouper", 10, 1))
    insert_product(conn, ("broccoli", 124, 9))
    insert_product(conn, ("cabbage", 80, 5))
    insert_product(conn, ("scallion", 53, 8))
    insert_product(conn, ("turnip", 89, 4))

# 8. Добавить функцию, которая меняет количество товара по id
def update_quantity(conn, product):
    sql = '''
    UPDATE products SET quantity = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# 9. Добавить функцию, которая меняет цену товара по id
def update_price(conn, product):
    sql = '''
    UPDATE products SET price = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)



# 10. Добавить функцию, которая удаляет товар по id
def delete_product(conn, product_id):
    sql = '''
    DELETE FROM products where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
def select_all_products(conn):
    sql = '''
    SELECT * from products 
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)


# 12. Добавить функцию, которая бы выбирала из БД товары
# которые дешевле 100 сомов и количество которых больше чем 5 и распечатывала бы их в консоли
def select_products(conn, limit):
    sql = '''
    SELECT * from products where price < ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)


# 13. Добавить функцию, которая бы искала в БД товары по названию
# (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием -
# “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)

def search_item(conn, search):
    search = '%' + search + '%'
    sql = '''
        SELECT * from products where product_title LIKE ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (search,))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)



connection = create_connection(db_name)
if connection is not None:
    print("Successfully connected to DB " + db_name)
    #create_table(connection, create_students_table_sql)
    #add_products(connection)
    update_quantity(connection, (4, 1))
    update_price(connection, (135, 1))
    select_all_products(connection)
    select_products(connection, 100)
    search_item(connection, "mutton")
    connection.close()
    print("DONE!")
