import psycopg2
from config import cursor, config

# Creating database
# Use exception handler because there is no IF NOT EXISTS option
try:
    create_database = f"CREATE DATABASE {config.DB_NAME};"
    cursor.execute(create_database)
except psycopg2.errors.DuplicateDatabase as e:
    print(e)
