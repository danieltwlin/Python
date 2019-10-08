#! python3
# coding: utf-8

# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

# 連接 MySQL 資料庫
db = MySQLdb.connect(host="localhost",
    user="nuser", passwd="pwd", db="my_db")
cursor = db.cursor()

# 執行 MySQL 查詢指令
cursor.execute("SELECT * FROM my_table")

# 取回所有查詢結果
results = cursor.fetchall()

# 輸出結果
for record in results:
  col1 = record[0]
  col2 = record[1]
  print( "%s, %s" % (col1, col2) )

# 關閉連線
db.close()
