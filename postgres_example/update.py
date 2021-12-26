from postgres_example.config import connection, cursor, config

# Executing update
cursor.execute(f"UPDATE {config.TABLE} SET name = %s WHERE name = %s", ("TEST", "Vasya1"))
connection.commit()

# Altering table
cursor.execute(f"ALTER TABLE {config.TABLE} DROP address")
connection.commit()

# Close connection
cursor.close()
connection.close()
