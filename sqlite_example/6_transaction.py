import sqlite3

con = sqlite3.connect("contacts_db.sqlite_example")

DB = 'contacts'

sql_1 = f"INSERT INTO {DB} (name, email, phone) VALUES (?, ?, ?)"
sql_2 = f"UPDATE {DB} SET name = ? WHERE email = ?"
sql_3 = f"DELETE FROM {DB} WHERE name = ?"

name = 'SuperUser'
new_name = 'NEW_USER'
email = 'superemail@email.ru'
address = 'California'


con.execute(sql_1, (name, email, "989898"))
con.execute(sql_2, (new_name, email))
con.commit()
con.rollback()
con.execute(sql_3, (name,))
con.rollback()
con.commit()

con.close()
