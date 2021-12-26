from sqlalchemy import Table
from sqlalchemy import MetaData, create_engine
from sqlalchemy import select, insert, delete
from maria_db_example.config import config

metadata = MetaData()
TABLE = "contacts"

# First we need to create the table
engine = create_engine(
    f'mysql+mysqlconnector://{config.USER}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DB_NAME}'
)

contacts = Table(TABLE, metadata, autoload=True, autoload_with=engine)

print(contacts.columns.keys())

# Prepare the request
s = select([contacts]).limit(2)

# Getting rows
rows = engine.execute(s).fetchall()

# Iterate over rows
for row in rows:
    print(row)

# Prepare and execute insert statement
i = insert(contacts).values(name="Test", email="test@mail.ru", phone="11111111111")
engine.execute(i)

# Delete the entry
# ds = delete(contacts).where(contacts.c.name == "Test")
# engine.execute(ds)

# List all data
# for row in engine.execute(select([contacts])).fetchall():
#     print(row)
