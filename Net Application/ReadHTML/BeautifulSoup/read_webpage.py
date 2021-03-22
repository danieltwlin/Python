# -*- coding: UTF-8 -*-
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup 
import requests 
import os
import time

# 檢查 dsc task 的 tick 狀態，為空字串則回傳 error 字串
# tick 若大於0，則為正常
def check_dsc_task(page):
	#page = 'http://xx.xx.xx.xx:8080/task.php' 

	html_doc = requests.get(page) 

	strs = html_doc.text.split('<br>')  # 讀取每行 

	error = ''

	for str in strs :
		key= 'server:'
		if( key in str):
			tmp =str.replace(key,'') # 去掉指定字串
			tmp = tmp.strip() # 去掉空白			
			
			if(len(tmp)>0):
				value =int(tmp)
				#print(value)
			else:
				error = 'DSC have error tag '
			
	return error
	
	
if __name__ == '__main__':
	
	# Dsc 三個站台
	pages = ['http://xx.xx.xx.xx:8080/task.php',
				'http://xx.xx.xx.xx:8080/task.php',
				'http://xx.xx.xx.xx:8080/task.php']
	
	
	for page in pages:
	
		error = ''
		
		error = check_dsc_task(page)
		
		if(error !=''):
			print( page + error)
		else:
			print( page + ' : DSC is OK !')


	
		
