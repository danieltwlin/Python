import time
import os

from datetime import datetime

# Strftime
now = datetime.now() # current date and time

date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
print("date and time:",date_time)




# 手工
import datetime

def get_time():
		x = datetime.datetime.now()
		# format space
		#dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
		dt = str(x.year)+'/'+str(x.month).zfill(2)+ '/'+str(x.day).zfill(2)+ ' '+ str(x.hour).zfill(2) + ':' + str(x.minute).zfill(2) + ':' + str(x.second).zfill(2)
		#print(dt)
		return dt
		
print(get_time())

### 上面是包裝好的，下面是未經包裝  ###

########################################
x = datetime.datetime.now()
# format space
dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
print(dt_now)
########################################
