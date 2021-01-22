import paramiko
import time
from getpass import getpass

ip = 'xx.xx.xx.xx'
username = 'username'
password = 'pwd'

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'cd /opt/py\n')
DEVICE_ACCESS.send(b'pwd\n')
time.sleep(5)
output = DEVICE_ACCESS.recv(65000)
#print(output.decode('ascii'))
print(output.decode())

SESSION.close 
