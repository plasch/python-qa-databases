from sqlite_example.config import connection, config

cursor = connection.cursor()

sql = f"INSERT INTO {config.TABLE} (name, email, phone, address) VALUES (?, ?, ?, ?)"
# data = ("Vasiliy", "vasiliy@mail.ru", "+79160001234", "Moscow")
#
# # We separate data from SQL statement as recommended
# cursor.execute(sql, data)

# Commit can be called only from connection!
# connection.commit()
#
all_data = [
    ("Vasiliy1", "vasiliy@mail.ru", "+79160001234", "Moscow1"),
    ("Vasiliy2", "vasiliy@mail.ru", "+79160001234", "Moscow2"),
    ("Vasiliy3", "vasiliy@mail.ru", "+79160001234", "Moscow3"),
    ("Vasiliy4", "vasiliy@mail.ru", "+79160001234", "Moscow4")
]

cursor.executemany(sql, all_data)
connection.commit()

connection.close()
