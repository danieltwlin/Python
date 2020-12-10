import requests

''' Demo JSON-RPC POST '''

def main():
	url = "https://xx.xx.xx.xx"

	# Payload
	payload = {
		"jsonrpc":"2.0",
		"id":1,
		"method":"Hello",
		"params":{
			"stdId":"123456",			
			"verifyCode": "abc-def-xyz",
			"verifyVer": "1.0.0",			
			"extraInfo":{
				"os": "windows",
				"serial": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
				"brokerHostList":[],
				"isAuth":"true"
			}
		}
	}
	
	response = requests.post(url, json=payload).json()
	
  print( response)
	print( response["result"]["token"])
	print( response["result"]["deviceId"])
	
  
  # Assert   
	token = response["result"]["token"]	
	
  assert "Bearer" not in token
	assert response["result"]["deviceId"] != "RdDevice!"


if __name__ == "__main__":
	main()
