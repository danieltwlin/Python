import requests

''' Demo Simple Get '''

def main():

	# newies tw
	url = "https://www.google.com"

	response = requests.get(url).json()
	
	print( response)
	
	#assert "200" not in Response Code
	assert response["code"] != "200"

if __name__ == "__main__":
	main()
