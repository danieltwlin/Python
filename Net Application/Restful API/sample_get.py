import requests
import json
''' Demo Simple Get '''

def main():

	# newies tw
	url = "https://www.google.com"

	response = requests.get(url).json()
	
	print( response)
	print( response.status_code)
	
	#assert "200" not in Response Code
	assert response["code"] != "200"

if __name__ == "__main__":
	main()
