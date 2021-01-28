import mysql.connector

mydb = mysql.connector.connect(
  host="abc",
  user="abc",
  password="abcd"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE user")