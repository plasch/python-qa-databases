import sqlite3
from sqlite_example.config import connection, config

cursor = connection.cursor()

# Delete table
# cursor.execute("DROP TABLE contacts2")
# cursor.execute(f"DROP TABLE IF EXISTS contacts2")

sql = f"DELETE FROM {config.TABLE} WHERE name = ?"
cursor.execute(sql, ("Vasiliy4",))
connection.commit()

connection.close()