from maria_db_example.config import connection, cursor

TABLE = "contacts"

SQL = f"""
CREATE TABLE IF NOT EXISTS {TABLE}
(
    id INT(32) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    score INTEGER
);
"""

# Creating table inside database
cursor.execute(SQL)
connection.commit()

# Inserting single data entry
sql = f"INSERT INTO {TABLE} (name, phone, email, address) VALUES (%s, %s, %s, %s)"
values = ("Vasya2", "+89009009999", None, "Moscow")
cursor.execute(sql, values)
connection.commit()
#
# # Inserting multiple lines
# values = [
#     ("Vasya000", "89009009569", None, "Moscow"),
#     ("Vasya2", "89009057699", None, "London"),
#     ("Vasya3", "89065709999", "no@mail.ru", "Minsk"),
#     ("Vasya5", "89009765999", None, "Petropavlovsk"),
# ]
#
# sql = f"INSERT INTO {TABLE} (name, phone, email, address) VALUES (%s, %s, %s, %s)"
# cursor.executemany(sql, values)
# connection.commit()
#
# cursor.close()
# connection.close()
