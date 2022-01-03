import mysql.connector
import os

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASS
)

cursor = mydb.cursor()

#cursor.execute("CREATE DATABASE todo")

#cursor.execute("drop database qpusers")

#for db in cursor:
#    print(db)