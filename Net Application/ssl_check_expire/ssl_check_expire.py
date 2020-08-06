from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
from pprint import pprint
from datetime import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import timedelta
from time import sleep
'''
Check websit ssl expire,and send dingding msg

'''
def get_ssl_expire_time_difference(base_url):

	#some site without http/https in the path
	port = '443'

	#base_url = 'google.com' # for test
	hostname = base_url
	#ssl._create_default_https_context = ssl._create_unverified_context()

	context = ssl.create_default_context()

	with socket.create_connection((hostname, port)) as sock:
		with context.wrap_socket(sock, server_hostname=hostname) as ssock:
			#print(ssock.version())
			data = json.dumps(ssock.getpeercert())

	# convert to dict type
	data2 = json.loads(data)
	#print(type(data2))
	#print( data2)

	# Get Expire Date
	expire = data2['notAfter']
	#print( 'expire date :' + expire)  # UTC +0

	# GMT String To GMT Time
	#dateString = "Oct 28 23:59:59 2020 GMT"
	dateString = expire
	dateFormatter = "%b %d %H:%M:%S %Y GMT"

	expire_time = datetime.strptime(dateString, dateFormatter)
	# Convert UTC + 8
	expire_time = expire_time + timedelta(hours =8)

	expire_date = expire_time.strftime('%Y-%m-%d %H:%M:%S ')
	# print( 'expire date : ' + expire_date )

	# Get Time Now
	t = datetime.now()

	# Calculate Time Difference

	d1 = expire_time
	#d1 = datetime(2020, 8, 3) # for test

	d2 = t

	dayCount = (d1 - d2).days

	#print( dayCount )

	return dayCount,expire_date


def ddmsg(msg, hookid=1):

	if(hookid == 1):
		#WebHook地址
		webhook = 'https://oapi.dingtalk.com/robot/send?access_token=XXXXX'
	if(hookid == 2):
		#WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=XXXXX'

	# 初始化机器人小丁
	xiaoding = DingtalkChatbot(webhook)

	#Text消息@所有人
	xiaoding.send_text(msg=msg, is_at_all=True)

def url_ssl_check( url ):

	#base_url = "ies.aclass.com.tw"
	base_url = url
	#print( base_url)

	days, expire_date = get_ssl_expire_time_difference(base_url)

	msg1 =  base_url + ' \n Expire Date : ' + expire_date
	msg1 =  msg1 + ' \n Expire days : ' + str(days) + ' days'
	msg2 =''

	if( days <= 0 ):
		msg2 = ' Alert : it was expired !!!! \n'

	if( (days > 0) and (days < 14)  ):
		msg2 = ' Alert : it is expiring soon !!!!\n'

	msg = msg1 + '\n' + msg2
	print(msg)

	if( len(msg2)>0):
		ddmsg(msg)


if __name__ == '__main__':

	# ies tw
	if(1):
		url = "google.com"
		url_ssl_check(url)
    
    
