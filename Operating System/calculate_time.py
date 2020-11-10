import os
import datetime,time

# Start Time
starttime = datetime.datetime.now()

#long running


#### DO SOMETHING ###
time.sleep(10)
# rsync code
os.system('sh nasrsync.sh')


# Get Total Time
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)

# Time Format
seconds = (endtime - starttime).seconds
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%02d:%02d:%02d" % (h, m, s))
