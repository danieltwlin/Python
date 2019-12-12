# -*- coding: UTF-8 -*-
#=== ftp Tool ================================
# Date   : 2019.12.11
# Author : daniel
# Caption: FTP login,Download,Upload Tool
#============================================
import os
import sys

# FTP操作
import ftplib

class FtpTool():
	def __init__(self, host,username,password):
		f = ftplib.FTP(host)  # 實例化FTP對象
		f.login(username, password)  # 登錄
		self.f = f
		## 獲取當前路徑
		#pwd_path = f.pwd()
		#print("FTP當前路徑:", pwd_path)	

	def ftp_login(self,host,username,password):
		''' FTP 登入 '''
		f = self.f
		f = ftplib.FTP(host)  # 實例化FTP對象
		f.login(username, password)  # 登錄

	def ftp_download(self,file_remote, file_local,bufsize = 1024):
		'''以二進制形式下載文件'''
		f = self.f
		#file_remote = '1.txt'
		#file_local  = 'D:\\test_data\\download.txt'
		#bufsize = 1024  # 設置緩沖器大小
		fp = open(file_local, 'wb')
		f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
		fp.close()


	def ftp_upload(self,file_remote, file_local,bufsize = 1024):
		'''以二進制形式上傳文件'''
		f = self.f
		#file_remote = 'upload.txt'
		#file_local  = 'D:\\test_data\\2.txt'
		#bufsize = 1024  # 設置緩沖器大小
		fp = open(file_local, 'rb')
		f.storbinary('STOR ' + file_remote, fp, bufsize)
		fp.close()
		
	def ftp_close(self):
		f = self.f
		f.quit()

if __name__ == '__main__':
	
	host = 'ftp_ip'
	username = 'user'
	password = 'pwd'
	
	# FTP init	
	f = FtpTool(host,username,password)
	
	## 下載
	file_remote = '1.txt'
	file_local  = 'D:\\test_data\\download.txt'
	f.ftp_download(file_remote,file_local)
	
	# 上傳
	file_remote = 'upload.txt'
	file_local  = 'D:\\test_data\\2.txt'
	f.ftp_upload(file_remote,file_local)
	
	# 結束
	f.ftp_close()
	