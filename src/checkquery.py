import mysql.connector
import config
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= config.mysql_db_password,
    database="devdb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM transaction_csnox")

for table in mycursor:
    print(table)