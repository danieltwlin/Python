import datetime,time
import os

# Start Time
starttime = datetime.datetime.now()

#long running
#time.sleep(2)


# code
os.system('sh nasrsync.sh')

# data
#os.system('sh nasrsync2.sh')


# Get Total Time
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)

# Time Format
seconds = (endtime - starttime).seconds
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%02d:%02d:%02d" % (h, m, s))
