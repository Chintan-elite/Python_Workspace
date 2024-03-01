import mysql.connector


myconn = mysql.connector.connect(

    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="pythonsql"
)

cursor = myconn.cursor()

# cursor.execute("create table emp(id int PRIMARY KEY auto_increment, name varchar(20), email varchar(30))")
cursor.execute("show tables")

for x in cursor:
    print(x)
