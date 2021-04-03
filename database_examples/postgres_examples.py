
import psycopg2

username = 'ujjwal.tak'
database = 'testdb'


def create_conn():
    conn = psycopg2.connect(database=database, user=username)
    # conn = psycopg2.connect(f"dbname={database} user={username}")
    print("successfully connected!")
    return conn


def create_store_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    # conn.close()
    return cur.statusmessage


def insert_data_into_store(conn, item, quantity, price):
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    # conn.close()
    return cur.rowcount


def fetch_data_from_store(conn, item=None):
    cur = conn.cursor()
    if item:
        cur.execute("select * from store where item = %s", (item, ))
    else:
        cur.execute("select * from store")
    result = cur.fetchall()
    # conn.close()
    return result


def delete_data_from_store(conn, item):
    cur = conn.cursor()
    cur.execute("delete from store where item = %s", (item, ))
    conn.commit()
    # conn.close()
    return cur.rowcount


def update_data_in_store(conn, item, quantity, price):
    cur = conn.cursor()
    cur.execute("update store set quantity=%s, price=%s where item = %s",
                    (quantity, price, item))
    conn.commit()
    # conn.close()
    return cur.rowcount


if __name__ == '__main__':
    _conn = create_conn()
    # resp = create_store_table(_conn)
    # print(resp)
    resp = insert_data_into_store(_conn, 'Peach', 11, 8.6)
    print(resp)
    resp = update_data_in_store(_conn, 'Peach', 10, 20.6)
    print(resp)
    resp = fetch_data_from_store(_conn)
    print(resp)
    resp = delete_data_from_store(_conn, 'Peach')
    print(resp)
    _conn.close()
