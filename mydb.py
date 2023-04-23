"""
1. install MySQL on your computer
2. https://dev.mysql.com/downloads/installer/
3. pip install mysql
4. pip install mysql-connector
5. pip install mysql-connector-python

"""
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'jonma0107'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE joncore")

print("All Done!")
