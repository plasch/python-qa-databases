from postgres_example.config import connection, cursor, config

# Добавление одного кортежа данных
sql = f"INSERT INTO {config.TABLE} (name, phone, email, address) VALUES (%s, %s, %s, %s)"

values = ('Test1', '8999999', 'a@mail.ru', 'Moscow')

cursor.execute(sql, values)
connection.commit()

values = [
    ("Vasya1", "+79009009999", None, "Moscow"),
    ("Vasya2", "+79009009999", None, "Minsk"),
    ("Vasya3", "+79009009999", None, "Vladivostok"),
    ("Vasya5", "+79009009999", None, "Berlin"),
]

cursor.executemany(sql, values)
connection.commit()

cursor.close()
connection.close()
