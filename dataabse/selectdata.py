import mysql.connector

myconn = mysql.connector.connect(

    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="pythonsql"
)

cursor = myconn.cursor()


cursor.execute("select * from emp")

mydata = cursor.fetchall()

# print(mydata)

for x in mydata:
    print(x)