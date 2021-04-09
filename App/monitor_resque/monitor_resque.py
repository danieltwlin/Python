import os
import sys
from dingtalkchatbot.chatbot import DingtalkChatbot

# Send DingMsg
def DingMsg(msg):
	#WebHook..
	webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxx'
	xiaoding = DingtalkChatbot(webhook)
	xiaoding.send_text(msg, is_at_all=True)

# execute command, and return the output
def execCmd(cmd):
	r = os.popen(cmd)
	text = r.read()
	r.close()
	return text

# find resque job
def check_resque(key,station):
	#ret  = execCmd('ps aux | grep coreapi_en/index.php')
	ret  = execCmd(key)
	print( ret)

	lst1 = ret.split('\n')
	#print(lst1[0])
	
	status = False

	# Check String
	for item in lst1 :
		#print(item)
		value = 'workers'
		if( value in item ):
			value = ' S '
			if( value in item):
				status = True
	
	# Check Status, And Send DingMsg
	if(status):
		msg = station + ' job is Ok'
		print( msg)
		DingMsg(msg)

	else:
		msg = station + ' job is Error'
		print( msg)
		DingMsg(msg)

'''	Check Resque Process	'''
if __name__ == '__main__':

	# check tw resque
	key = 'ps aux | grep coreapi/index.php'
	check_resque(key,'resque tw')

	# check en resque
	key = 'ps aux | grep coreapi_en/index.php'
	check_resque(key,'resuqe en')
