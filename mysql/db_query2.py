# coding: utf-8
import os,sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import datetime
import pytz
import types

'''
DATE : 2021/07/02
AUTHER: Daniel
'''

# query db
def db_query(cmd):
        db = MySQLdb.connect(host="localhost",
            user="backup", passwd="backup", db="sokradeo",charset="utf8")
        cursor = db.cursor()

        # .. MySQL ....
        cursor.execute(cmd)

        # ........
        result = cursor.fetchall()
        #print(result)

        #if(0):
        #       # ....
        #       for record in results:
        #               col1 = record[0]
        #               col2 = record[1]
        #       print( "%s, %s" % (col1, col2) )

        # close
        db.close()

        return result    

if __name__ == "__main__":
  
       #cmd = "SELECT  *  from tb1 where id=123 and date_format( created_at, '%Y-%m-%d %H')=date_format(  NOW()+INTERVAL 8 HOUR, '%Y-%m-%d 05')  and name ='IRS' LIMIT 1"
       cmd = "SELECT  *  from tb1 where id=123"
      
       ret = db_query(cmd)

        # No Vedio Data
        if(len(ret)== 0):
                print("0")                
        else:
                num =ret[0][0]
                num=str(num)
                print( num)
                

      
