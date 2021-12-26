import psycopg2

from types import SimpleNamespace
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

config = SimpleNamespace(
    DB_NAME='contacts_db',
    TABLE='contacts',
    HOST='192.168.1.95',
    PORT='5432',
    USER='postgres',
    PASSWORD='root',
)

connection = psycopg2.connect(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT,
    database=config.DB_NAME
)

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Getting cursor object from connection
cursor = connection.cursor()
