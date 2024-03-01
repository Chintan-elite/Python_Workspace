import mysql.connector

myconn = mysql.connector.connect(

    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="pythonsql"
)

cursor = myconn.cursor()

qry = "insert into emp(id,name,email)values(%s,%s,%s)"
# val = (1,"chintan","chintan@gmail.com")
# cursor.execute(qry,val)

val = [(2,'kinjal','kinju@gmil.com'),(3,'dipu','dipu@gmail.com')]
cursor.executemany(qry,val)
myconn.commit()
print(cursor.rowcount)
print(cursor.lastrowid)