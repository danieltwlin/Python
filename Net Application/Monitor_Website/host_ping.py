import os
import sys

iplist = list()
ip = '192.168.1.228'   # or domain like 'http://www.goog.com'

result =  os.system('ping -c 1 -w 3 %s'%ip) #    -c  times, -w wait second

print('backinfo: '+ str(result ))
#print(type(result))

# success return 0

if(result):
        print('ping error : ' + ip )
        raise(RuntimeError( ip + ' PC is not survive !'))
else:
        iplist.append(ip)
        print('ping success : ' + ip )

print(iplist)


