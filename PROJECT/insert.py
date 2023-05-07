import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Preethi@12345",database="inventorycontrolmanagement")
cur=mydb.cursor()
e1 = 'insert into manufacture(PRODUCT_ID,PRODUCT_NAME,MANUFACTURED_COMPANY,MANUFACTURED_DATE,NEED_TO_BE_MANUFACTURED,NO_OF_ITEMS_MANUFACTURED,NO_OF_DEFECTIVE_ITEMS,MANUFACTURED_AMOUNT) values (%s,%s,%s,%s,%s,%s,%s,%s)'
v1= [(111,'Wooden Chair','SS Exports','2023-04-29',100,100,5,50000),
(112,'Wooden Table','SS Exports','2023-04-29',100,100,7,100000),
(113,'red-colored-toys','ABC Exports','2023-04-29',200,200,15,40000),
(114,'shirt','AHSH Exports','2023-04-29',300,300,3,240000),
(113,'red-colored-toys','ABC Exports','2023-04-30',200,200,15,40000),
(114,'shirt','AHSH Exports','2023-04-30',300,300,3,240000),
(113,'red-colored-toys','ABC Exports','2023-05-01',200,200,6,40000),
(114,'shirt','AHSH Exports','2023-05-01',300,300,18,240000)]

e1='INSERT INTO GOODS(PRODUCT_ID,PRODUCT_NAME,MANUFACTURED_COMPANY ,MANUFACTURED_DATE,AVAILABLE_QUANTITY,COST_OF_EACH_ITEM )VALUES(%s,%s,%s,%s,%s,%s)'
v1 = [(111,'Wooden Chair','SS Exports','2023-05-01',60,500),
(112,'Wooden Table','SS Exports','2023-05-01',40,1000), 
(113,'red-colored-toys','ABC Exports','2023-05-01',70,200), 
(114,'shirt','AHSH Exports','2023-04-30',60,800),
(113,'red-colored-toys','ABC Exports','2023-05-02',60,200), 
(114,'shirt','AHSH Exports','2023-05-02',50,800),
(113,'red-colored-toys','ABC Exports','2023-05-03',50,200), 
(114,'shirt','AHSH Exports','2023-05-03',40,800)]

e1='INSERT INTO PURCHASE(PRODUCT_ID,PRODUCT_NAME,PURCHASE_ID,PURCHASE_DATE,PURCHASE_STORE,PURCHASE_MODE,PURCHASE_QUANTITY,PURCHASE_AMOUNT,DEFECTIVE )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
v1 = [(111,'Wooden Chair',511,'2023-05-05','MyCare','online',70,35000,0),
(112,'Wooden Table',512,'2023-05-05','MyCare','offline',60,60000,0),
(113,'red-colored-toys',513,'2023-05-05','MyKids','offline',80,16000,0),
(114,'shirt',514,'2023-05-05','ORay','online',65,52000,0),
(113,'red-colored-toys',513,'2023-05-05','MyKids','offline',30,6000,1),
(114,'shirt',514,'2023-05-05','ORay','online',20,16000,1),
(113,'red-colored-toys',513,'2023-05-06','MyKids','offline',80,16000,0),
(114,'shirt',514,'2023-05-06','ORay','online',65,52000,0)]

e1='INSERT INTO SALES(PRODUCT_ID,PRODUCT_NAME ,SALES_QUANTITY ,SALES_DATE ,SALES_AMOUNT ,PROFIT_MARGIN )VALUES(%s,%s,%s,%s,%s,%s)'
v1=[ (111,'Wooden Chair',70,'2023-05-10',49000,14000),
(112,'Wooden Table',60,'2023-05-10',72000,12000),
(113,'red-colored-toys',80,'2023-05-10',24000,8000),
(114,'shirt',65,'2023-05-10',65000,13000),
(113,'red-colored-toys',80,'2023-05-11',24000,8000),
(114,'shirt',65,'2023-05-11',65000,13000)]
cur.executemany(e1,v1)
mydb.commit()
print("inserted successfully")


# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, 
# manufactured on the date ‘01-04-23’.
t='DELETE P FROM PURCHASE P JOIN MANUFACTURE M ON M.PRODUCT_ID = P.PRODUCT_ID WHERE PURCHASE_STORE="ORay" AND DEFECTIVE=1 AND M.MANUFACTURED_DATE="2023-04-29"'
cur.execute(t)

# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
t='UPDATE MANUFACTURE M JOIN PURCHASE P ON P.PRODUCT_ID = M.PRODUCT_ID SET NEED_TO_BE_MANUFACTURED = NEED_TO_BE_MANUFACTURED+PURCHASE_QUANTITY WHERE M.PRODUCT_NAME = "red-colored-toys" AND P.PURCHASE_STORE="MyKids"'
cur.execute(t)


# Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
t='SELECT * FROM MANUFACTURE WHERE PRODUCT_NAME="Wooden Chair" AND MANUFACTURED_DATE <="2023-05-01"'
cur.execute(t)


# Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, 
# manufactured by the “SS Export” company.
t='SELECT SUM(PROFIT_MARGIN) FROM SALES S JOIN PURCHASE P ON P.PRODUCT_ID = S.PRODUCT_ID JOIN MANUFACTURE M ON M.PRODUCT_ID = S.PRODUCT_ID  WHERE S.PRODUCT_NAME="Wooden Table" AND P.PURCHASE_STORE = "MyCare" AND M.MANUFACTURED_COMPANY = "SS Exports"'
cur.execute(t)


