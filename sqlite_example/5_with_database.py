from sqlite_example.config import connection, config

cursor = connection.cursor()

with open("table.sql", "r") as script:
    cursor.execute(script.read())

sql = f"INSERT INTO {config.TABLE} (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("One", "Two", "Three", "Four")

# https://docs.python.org/3.7/library/sqlite3.html

with connection:
    cursor.execute(sql, data)


connection.close()
