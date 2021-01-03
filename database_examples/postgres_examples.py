
import psycopg2

username = 'ujjwal.tak'
database = 'testdb'


def create_conn():
    conn = psycopg2.connect(database=database, user=username)
    print("successfully connected!")
    return conn


if __name__ == '__main__':
    create_conn()
