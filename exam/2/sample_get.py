# -*- coding: utf8 -*-
import os,sys
import requests
''' Demo Simple Get '''

def sample_get():

	# url
	url = "https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789"
	print("url = " + url)
	response = requests.get(url)
	print("Response Code " + str(response.status_code))
	# Assert Response Code is 200
	assert response.status_code == 200

	url = "https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1"
	print("url = " + url)
	response = requests.get(url)
	print("Response Code " + str(response.status_code))	
    # Assert Response Code is 403
	assert response.status_code == 403
	
if __name__ == "__main__":
	sample_get()
