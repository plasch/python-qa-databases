# Guide for mysql docker setup

```
docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ROOT_HOST=% mysql/mysql-server
docker exec -it {CONTAINER_ID} bash

bash-4.2# 
mysql -p
Enter password: root
create database contacts_app;
connect {database_name}

show databases; 
show tables;
drop database; 
drop table;
```
