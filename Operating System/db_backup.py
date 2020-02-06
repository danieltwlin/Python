mport time
import os
import datetime

x = datetime.datetime.now()

# format space
# dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
# print(dt_now)

# get date
print( 'Today Number: ' )
print(str(x.day).zfill(2))

number =str(x.day).zfill(2)

# backup db
cmd = 'cp publicitem.sql ./backup/publcitem_' + number + '.sql'
os.system(cmd)

cmd = 'cp answerinfo.sql ./backup/answerinfo_' + number + '.sql'
os.system(cmd)

cmd = 'cp learncenter.sql ./backup/learncenter_' + number + '.sql'
os.system(cmd)
