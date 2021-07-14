import os
import mysql.connector
from time import sleep
from time import time


# Update DB
mydb=''
if(1):
        mydb = mysql.connector.connect(
          host="192.168.xx.xx",
          user="root",
          passwd="xxxx"
        )

        mycursor = mydb.cursor()

if(1):
        # Drop DB If Exist
        mycursor.execute("DROP DATABASE IF EXISTS  DB1;")
        # Drop DB If Exist
        mycursor.execute("DROP DATABASE IF EXISTS  DB2;")

        # Create DB
        mycursor.execute("CREATE DATABASE DB1 DEFAULT CHARSET utf8 COLLATE utf8_unicode_ci; ")
        mycursor.execute("CREATE DATABASE DB2 DEFAULT CHARSET utf8 COLLATE utf8_unicode_ci; ")

        # Close sql Connection
        mydb.close()

# Import SQL File
if(1):
        print('Import SQL file')
        os.chdir('/opt/DB')

        if(1):
                print('Import DB1.sql')
                os.system('mysql -h192.168.xx.xx -uroot -pxxxx DB1 < DB1.sql')
                print('Import DB1.sql finish')
                sleep(3)
        if(1):
                print('Import DB2.sql')
                os.system('mysql  -h192.168.xx.xx -uroot -pxxxx DB2 < DB2.sql')
                print('Import DB2.sql finish')
 
