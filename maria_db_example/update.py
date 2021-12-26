from maria_db_example.config import config
from maria_db_example.config import connection, cursor

# Executing update query
cursor.execute(f"UPDATE {config.TABLE} SET name = %s WHERE name = %s", ("TEST", "Vasya1",))
connection.commit()

# Altering given table
cursor.execute(f"ALTER TABLE {config.TABLE} DROP address")
connection.commit()

# Closing cursor and connection
cursor.close()
connection.close()
