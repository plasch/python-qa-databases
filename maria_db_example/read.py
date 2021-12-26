from maria_db_example.config import config
from maria_db_example.config import connection, cursor

# Выполняем запрос
cursor.execute(f"SELECT * FROM {config.TABLE}")

# Пример вычитывания курсора.
# Getting all available rows
for row in cursor.fetchall():
    print(row)

# Getting first entry
print(cursor.fetchone())
cursor.reset()

cursor.execute(f"SELECT * FROM {config.TABLE} WHERE name = 'Afghanistan'")

if cursor.fetchall():
    print("Record exists!")
else:
    print("Not exists!")

# Close connection and cursor
cursor.close()
connection.close()
