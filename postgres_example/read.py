from postgres_example.config import connection, cursor, config

# Выполняем запрос
cursor.execute(f"SELECT * FROM {config.TABLE};")

# Получаем данные в виде кортежей
for row in cursor.fetchall():
    print(row)

# Закрываемся
cursor.close()
connection.close()
