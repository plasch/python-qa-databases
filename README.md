# Работа с СУБД

##  Python

Python API - https://www.python.org/dev/peps/pep-0249/

Libraries:

- https://docs.python.org/3/library/sqlite3.html
- https://pypi.org/project/mysql-connector-python/

## Терминология

CRUD (CREATE, READ, UPDATE, DELETE) - Базовый набор операций которые необходимы для работы с БД

## Основы работы

1) Create connection

```python
import sqlite3

connection = sqlite3.connect("simple.sqlite_example")
cursor = connection.cursor()
```

```python
import mysql.connector

connection = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')
cursor = connection.cursor()
```

```python
import psycopg2

connection = psycopg2.connect(user='db_user', password='mypassword', dbname='database', host='localhost')
cursor = connection.cursor()

```

2) CRUD

```python
# SQLite
sql = "INSERT INTO {DB_NAME} (name, email, phone, address) VALUES (?, ?, ?, ?)".format(DB=DB_NAME)
data = ("Vasiliy", "vasiliy@mail.ru", "+7999999999", "Moscow")
connection.execute(sql, data)
connection.commit()
```


3) Close connection

```python
connection.close()
```
