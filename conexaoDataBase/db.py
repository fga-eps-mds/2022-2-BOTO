from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    password='211041295', ## usar senha do seu DB
    database='BOTO'
)

@contextmanager
def nova_con():
    con = connect(**parametros)
    try:
        yield con
    finally:
        if(con and con.is_connected()):
            con.close()