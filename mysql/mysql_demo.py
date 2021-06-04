''' mysql example '''

import mysql.connector

# Connect , default port = 3306
mydb = mysql.connector.connect(
  host="192.168.0.233",
  user="daniel",
  passwd="daniel",
  database="RD_Monitor"
)

print(mydb)
mycursor = mydb.cursor()

# Query
if(0):

	mycursor.execute("SELECT * FROM AppStoreVersion")
	myresult = mycursor.fetchall()

	for x in myresult:
		print(x)

# Insert
if(1):
	sql = "INSERT INTO  AppStoreVersion(Product,Status,Play_Version,Baidu_Version ) VALUES (%s, %s, %s, %s)"
	val = ("myApp",'OK',"1.2.3.00","1.2.3.00")
	mycursor.execute(sql, val)
	
	mydb.commit()
	
	print(mycursor.rowcount, "record inserted.")
		
# update
if(0):		
	sql = "UPDATE test_table SET version = '1.2.3' WHERE id = '1'"

	mycursor.execute(sql)

	mydb.commit()

	print(mycursor.rowcount, "record(s) affected")	
