#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打開一個檔案，並讀取每一行

f = open("D:\\Code\\digicert.cer")
print("文件名为: ", f.name)  

k = f.readlines()   #读取一行  
print(k)
f.close()

 
##  依次读取每行
#
# for line in fo.readlines():                            
#    line = line.strip()                             #去掉每行头尾空白  
#    print "读取的数据为: %s" % (line)
# 
