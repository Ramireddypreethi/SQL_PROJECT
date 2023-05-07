import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Preethi@12345",database="inventorycontrolmanagement")
# password is different for everyone
print(mydb.connection_id)
cur=mydb.cursor()
t='CREATE TABLE GOODS (PRODUCT_ID INTEGER NOT NULL,PRODUCT_NAME VARCHAR(30) NOT NULL,MANUFACTURED_COMPANY VARCHAR(30) NOT NULL,MANUFACTURED_DATE DATE NOT NULL,AVAILABLE_QUANTITY INTEGER NOT NULL,COST_OF_EACH_ITEM INTEGER NOT NULL)'
cur.execute(t)