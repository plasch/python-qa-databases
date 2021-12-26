from sqlalchemy import Table
from sqlalchemy import MetaData, create_engine
from sqlalchemy import select, insert

from sqlite_example.config import config

metadata = MetaData()

# First we need to create the table
engine = create_engine(f'sqlite:///../sqlite/{config.DB_NAME}')

# Getting keys from table
contacts = Table(config.TABLE, metadata, autoload=True, autoload_with=engine)
print(contacts.columns.keys())

# # Prepare the request
s = select([contacts]).limit(2)

# Getting rows
rows = engine.execute(s).fetchall()

# # Iterate over rows
for row in rows:
    print(row)

# Prepare and execute insert statement
i = insert(contacts).values(name="Test", email="test@mail.ru", phone="11111111111")
engine.execute(i)
