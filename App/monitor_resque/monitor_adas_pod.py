import os

# execute command, and return the output
def execCmd(cmd):
	r = os.popen(cmd)
	text = r.read()
	r.close()
	return text

# get pod id
def get_pod(cmd):

	#print(cmd)
	#ret  = execCmd('kubectl get pods | grep adas')
	ret  = execCmd(cmd)
	#print( ret)

	lst1 = ret.split()
	#print(lst1)

	pod = lst1[0]
	print(pod)

	return pod

# get pod process status
def get_pod_process_status(cmd, key):

	print(cmd)
        #ret  = execCmd("kubectl exec podid '/opt/lampp/lampp status)")
	ret = execCmd(cmd)
	print( ret)

	status =  False

	#print(key)

	if( key in ret):
		status = True

	return status

def start_pod_apache(pod,cmd):

	kubecmd = 'kubectl exec ' + pod + ' -- ' + cmd
	print( kubecmd +'\n')
	ret = execCmd(kubecmd)
	#print(ret)
	return ret

'''	Check adas pod	'''
if __name__ == '__main__':

	cmd = 'kubectl get pods | grep adas'

	pod = get_pod(cmd)

	cmd = "kubectl exec "+ pod + " -- /opt/lampp/lampp status"
	key = "Apache is running."
	status = get_pod_process_status(cmd,key)

	#status = False
	if( status):
		print('ADAS job is Ok!')
	else:
		cmd = '/opt/lampp/lampp start'
		ret = start_pod_apache(pod,cmd)
		alertMsg = 'ADAS job is Error!, But alday execute ADAS job start command !'
		print(alertMsg)
		print('\n' + ret)

		raise RuntimeError(alertMsg)
	
