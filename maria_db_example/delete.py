from maria_db_example.config import config
from maria_db_example.config import connection, cursor

# Choose database
cursor.execute(f"USE {config.DB_NAME}")

# Executing query
cursor.execute(f"DELETE FROM {config.TABLE} WHERE name = %s", ("Vasya5",))
connection.commit()

# Close database
connection.close()
