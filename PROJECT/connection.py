import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Preethi@12345")
# password is different for everyone
print(mydb.connection_id)
cur=mydb.cursor()# cursor is a function
#CREATE SOME TEMPORARY MEMORY FOR USING OR CREATING DATABASE, TABLE.-- cursor()
cur.execute('create database InventoryControlManagement') 