import mysql.connector
from types import SimpleNamespace

config = SimpleNamespace(
    DB_NAME='bitnami_opencart',
    TABLE='oc_country',
    HOST='192.168.0.106',
    PORT='3306',
    USER='bn_opencart',
    PASSWORD='',
)

connection = mysql.connector.connect(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT,
)

# Getting cursor object from connection
cursor = connection.cursor()

# Switch to created database
cursor.execute(f"USE {config.DB_NAME}")

if __name__ == "__main__":
    # Creating database
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME} DEFAULT CHARACTER SET 'utf8'")
