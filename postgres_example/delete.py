from postgres_example.config import connection, cursor, config

# Execute delete data query
cursor.execute(f"DELETE FROM {config.TABLE} WHERE name='TEST'")
connection.commit()

# CLosing connections
cursor.close()
connection.close()