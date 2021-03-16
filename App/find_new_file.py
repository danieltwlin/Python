#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from os import listdir
from os.path import isfile, isdir, join

# 找到指定資料夾下的檔案
def find_files(folder, filter=""):
	# 指定要列出所有檔案的目錄
	#mypath = "d://"
	mypath =folder
	
	# 取得所有檔案與子目錄名稱
	files = listdir(mypath)

	filenames=[]
	
	# 以迴圈處理
	for f in files:
		# 產生檔案的絕對路徑
		fullpath = join(mypath, f)
		# 判斷 fullpath 是檔案還是目錄
		if isfile(fullpath):
			# 增加過濾條件
			if('.txt' in f):
				print("檔案：", f)
				filenames.append(fullpath)
		elif isdir(fullpath):
			print("目錄：", f)
		
	#print(filenames)
		
	return filenames

# 找到最新建立的檔案
def get_new_file(list):
	
	file1 =  list[0]
	t1 = os.path.getctime(file1)
	
	# 比較檔案時間
	for file in list:
		t2= os.path.getctime(file)  # getmtime: Modify, getatime: Access
		if( t2 > t1):
			t1= t2
			file1= file
	
	return file1	
		
if __name__ == '__main__':

	list =[]
	# 設定資料夾
	folder = "D:\\test"
	
	list = find_files(folder)
	file = get_new_file(list)
	print(list)
	print(file,time.ctime(os.path.getctime(file)))
