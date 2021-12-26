from sqlite_example.config import connection, config


cursor = connection.cursor()

# Bad example because hardcoded data!!!
sql = f"UPDATE {config.TABLE} SET email = 'TEST' WHERE name = ?"

cursor.execute(sql, ("Vasiliy",))
connection.commit()

sql = "UPDATE contacts_app SET name = ? WHERE name = ?"
data = ("HELLOTEST", "Vasiliy")

cursor.execute(sql, data)
connection.commit()

connection.close()